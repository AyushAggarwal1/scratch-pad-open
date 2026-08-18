import json
import subprocess
import time

from flask import Flask, request

QRADAR_IP = "181.0.79.227"  # change to QRadar IP if remote
QRADAR_PORT = 514

MAX_RETRIES = 3

app = Flask(__name__)


def restart_ipsec():
    try:
        print("Restarting ipsec...")
        subprocess.run(["ipsec", "stop"], capture_output=True)
        time.sleep(1)
        subprocess.run(["ipsec", "start"], capture_output=True)
        time.sleep(1)
        print("ipsec restarted")
    except Exception as e:
        print("ERROR restarting ipsec:", e)


def send_to_qradar_syslog(message):
    # Normalize to bytes
    if isinstance(message, str):
        data = message.encode("utf-8")
    else:
        data = message  # assume already bytes

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Attempt {attempt}: sending via nc to {QRADAR_IP}:{QRADAR_PORT}")
            # This is equivalent to: echo "<134>..." | nc -u -w1 <QRadar IP> <QRadar Port>
            proc = subprocess.run(
                ["nc", "-w1", QRADAR_IP, str(QRADAR_PORT)],
                # ["nc", "-u", "-w1", QRADAR_IP, str(QRADAR_PORT)],
                input=data,
                capture_output=True,
            )

            print("nc return code:", proc.returncode)

            if proc.stdout:
                print("nc stdout:", proc.stdout.decode().strip())
            if proc.stderr:
                print("nc stderr:", proc.stderr.decode().strip())

            # Success
            if proc.returncode == 0:
                print("Message successfully sent to QRadar")
                return True

            # Failure
            print("nc failed, restarting ipsec")
            restart_ipsec()

            if attempt < MAX_RETRIES:
                backoff = attempt  # 1s, 2s, 3s
                print(f"Retrying in {backoff} seconds...")
                time.sleep(backoff)

        except Exception as e:
            print("ERROR sending to QRadar via nc:", e)
            restart_ipsec()

            if attempt < MAX_RETRIES:
                backoff = attempt
                print(f"Retrying in {backoff} seconds...")
                time.sleep(backoff)

    print("All retry attempts failed")
    return False


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True, silent=True) or {}
    payload = json.dumps(data)

    syslog_msg = f"{payload}"
    print("Received webhook:", data)
    print("Sending to QRadar:", syslog_msg)

    send_to_qradar_syslog(syslog_msg)

    return "OK", 200


if __name__ == "__main__":
    # make sure this matches your curl (8081)
    app.run(host="0.0.0.0", port=8081)
