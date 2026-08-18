function exportSheetToJsonAndSaveToDrive() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = sheet.getDataRange().getValues();
    const jsonOutput = [];

    for (let i = 1; i < data.length; i++) {
        const row = data[i];
        jsonOutput.push({
            "Program Name": row[0],
            "Control Name": row[1],
            "Control Description": row[2],
            "Plugin Name": row[3],
            "Description": row[4],
            "Severity": row[5],
            "Recommended Action": row[6],
            "Link": row[7],
            "Domain": row[8],
            "Tags": row[9],
            "Remediation Steps": row[10],
            "more_info": row[11]
        });
    }

    const jsonString = JSON.stringify(jsonOutput, null, 2);
    const fileName = "exported_controls.json";

    // Create the file and get its link
    const file = DriveApp.createFile(fileName, jsonString, "application/json");
    const fileUrl = file.getUrl();

    Logger.log(`✅ JSON file saved: ${fileUrl}`);
}

exportSheetToJsonAndSaveToDrive();









// when all in single row

function exportPluginsToJson() {
    const ss = SpreadsheetApp.getActive();
    const sheet = ss.getActiveSheet(); // or ss.getSheetByName('Sheet1');

    const dataRange = sheet.getDataRange();
    const values = dataRange.getValues();
    const rows = values.slice(1); // skip header row

    const result = [];

    rows.forEach(row => {
      const dpdpControlId = row[0];        // Column A
      const dpdpControlName = row[1];      // Column B
      const dpdpControlDesc = row[2];      // Column C
      const pluginsCell = row[3];          // Column D

      if (!pluginsCell) return;

      const plugins = String(pluginsCell).split(/\r?\n/);

      plugins.forEach(plugin => {
        const pluginName = plugin.trim();
        if (!pluginName) return;

        result.push({
          // dpdpControlId: dpdpControlId,
          // dpdpControlName: dpdpControlName,
          // dpdpControlDescription: dpdpControlDesc,
          // pluginName: pluginName,
          "Program Name": "Digital Personal Data Protection (DPDP) Act India",
          "Control Name": dpdpControlId + " " + dpdpControlName,
          "Control Description": dpdpControlDesc,
          "Plugin Name": pluginName,
          "Description": "",
          "Severity": "",
          "Recommended Action": "",
          "Link": "",
          "Domain": "",
          "Tags": "",
          "Remediation Steps": "",
          "more_info": ""
        });
      });
    });

    const jsonString = JSON.stringify(result, null, 2);

    const fileName = "dpdp_plugins_export.json";

    // Create the file and get its link
    const file = DriveApp.createFile(fileName, jsonString, "application/json");
    const fileUrl = file.getUrl();

    Logger.log(`✅ JSON file saved: ${fileUrl}`);
  }
