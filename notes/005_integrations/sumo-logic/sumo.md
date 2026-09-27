---
title: Sumo Logic
parent: Integrations
grand_parent: Notes
nav_order: 2
description: "Setting up a Sumo Logic hosted or installed collector, plus the rsyslog forwarding config for VM sources."
---

# Sumo Logic


## Sumo Config

1. Sign-In to Platform
2. Go to **Data Management**
3. Add **Collection**

Type Hosted Collector (Sumo Cloud)
4. Now, Inside the Collection add **Source** as **HTTP Logs and Metrics** 
    - Copy Enpoint
        - Header - x-sumo-token: ZaVnC4dhaV3m0rN4

        - Endpoint - https://endpoint4.collection.sumologic.com/receiver/v1/http
5. Most Imp, Now Go to **Source** -> **Advance Option** for Log and Disable **Message Processing**

Type Installed Collector (VM)
4. Now, Inside the Collection add **Source** as **Installed Collector** 
5. Run the Script Shown on Sumo UI
6. Give chmod 0777 to script and run it
7. Select Access Token (Administration -> Account Security Settings -> Installation Token -> Generate New)
8. Device will Automatically Added
9. Add **Source** as Rsyslog
10. Make Sure in VM UDP 514 Port is Enabled and Recieving Alerts (*.* @127.0.0.1:1514)

## Rsyslog Configs
- Rsyslog Config Folder (cd /etc/rsyslog.d)
- Create a New Config (nano /etc/rsyslog.d/60-sumo-forward.conf)
- Add (*.* @127.0.0.1:1514)
