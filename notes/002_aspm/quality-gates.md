---
title: Quality Gates Flow
parent: ASPM
grand_parent: Notes
nav_order: 4
description: "How a CLI-embedded quality-gate policy blocks a CI pipeline until AccuKnox returns a pass/fail result."
---

## Quality Gates Flow

1. User Creates a Rule Engine with having set of conditions
  - A New, Not Mandatory/ Optional Action with Use as Quality Gates
  - Policy Id is generated and it will embeded in CLI
  - Use Attribute instead of Policy ID

2. User Runs the Scans 
  - CLI generate .json file with some metadata as
    ```JSON
      {
        "run_id"       : "XYZ",
        "commit_id"    : "XYZ",
        "run_number"   : "XYZ", 
        "asset_name"   : "XYZ",
        "branch"       : "XYZ"
      }
    ```
  - CLI push file to `artifact_api` with 1 or 2 new optional param as `policy_id` and `quality_gates` as `ENABLED/ DISABLED`
  - Now Here CI is running (not failed/ not passed/ not completed)
  - Refer PT 4.

3. AccuKnox Side
  - Do Simple Parsing
  - AccuKnox has
    - Asset Name
    - Vulnerabilites (breakdown in Crital, High, Medium, Low, Info)
    - With Metata
      ```JSON
        {
          "run_id"       : "XYZ",
          "commit_id"    : "XYZ",
          "run_number"   : "XYZ", 
          "asset_name"   : "XYZ",
          "branch"       : "XYZ"
        }
      ```
  - After Parsing Trigger Policy that comes in Artifact API
  - Store Result (PASS/ FAIL) of Quality Gate W.R.T to Policy ID and Asset Name, Branch, Run ID, Commit ID, Run Number
  - Expose a New Enpoint `get-policy-result` with above params, with having statuses as:
    - PENDING RESULT, POLICY PASSED, POLICY FAILED (EXPLOITED)

4. As Mentioned above (PT. 2) CI is Running 
  - CI can Poll Result from Endpoint (get-policy-result)
  - If POLICY PASSED then PASS the Pipeline 
    else if PENDING RESULT, sleep for 10 mins or X mins, send request again
    then POLICY FAILED means Pipeline Failed

