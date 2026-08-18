---
title: DSPM Overview & Onboarding
parent: DSPM
grand_parent: Notes
nav_order: 1
description: "Onboarding flow, MVP scan services per cloud, supported file formats, and Event-Trail log types for the DSPM engine."
---

**DSPM**

Cyera - https://www.youtube.com/watch?v=3KHidWuaiDI

**Ref Docs**
    - https://github.com/accuknox/dspm-active-scanner
    - https://github.com/accuknox/dspm-active-scanner/blob/main/design/iterations/generated/001-scanner.md

**Onboarding**
- User Select Cloud Account Type (AWS, Azure, GCP, OCI)
- Enable DSPM (Data Security Posture Management)
- User Create Token 
    - 2 Types
        - Artifact Token
        - Refresh Token   (for sending logs to accuknox -> Event-Trail)
- Scan Types/ Services 

| Cloud | MVP Services                                  |
| ----- | --------------------------------------------- |
| AWS   | S3, EBS Snapshots, RDS Snapshots, EC2 Volumes |
| Azure | Blob Storage, Managed Disks                   |
| GCP   | Cloud Storage, Persistent Disks               |
| OCI   | Object Storage                                |

- Scan Based on 
    A. Name
    B. Tag  - Include or Exclude
- List Permission
- Creds (Role ARN/ Assume Role)
- Scipt to Deploy DSPM ENGINE/ Service

**Action Items**
1. Need a terraform script/ Cloudformation (AWS) to Spin the DSPM VM/ Engine
2. DSPM Service Log Generation and Push to Event-Trail
    - DSPM_ENGINE_HEALTH
    - DSPM_ENGINE_STARTED
    - DSPM_ENGINE_STOPPED
    - SCAN_CREATED
    - SCAN_STARTED
    - SCAN_COMPLETED
    - SCAN_FAILED
    - ARTIFACT_UPLOADED

3. DSPM Engine Produces a JSON as Output 
    - Based on Per Scan Type,
    - Push Data to Artifact
4. DSPM Parser
    - Assets
    - Findings

**DSPM Engine**
- Scanners
    - Regex + Presidio Pre-defined Recognizers [Here](https://github.com/microsoft/presidio/tree/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific)
    - Lite ML Models (To Reduce False-Positive)
- Supported File formats

| Category        | Type                | Formats |
|-----------------|---------------------|---|
| Structured      | Spreadsheets        | `csv`, `xls`, `xlsx`, `tsv` |
| Semi-structured | Configuration files | `env`, `json`, `properties`, `xml`, `yml`, `yaml`, `tfstate` |
| Unstructured    | Documents           | `pdf`, `docx`, `doc`, `txt`, `log` |
| Unstructured    | Secrets             | `secrets`, `secret`, `rsa`, `ppk`, `pfx`, `pem`, `keys`, `key`, `p12`, `keystore`, `asc`, `jks` |
| Unstructured    | Images              | `tiff`, `jpg`, `gif`, `bmp`, `jpeg`, `png` |
| Compressed      | Archives            | `zip`, `tar`, `bz2`, `gz` — only if contents include a supported format above |

- Per File Size 

- VM Size??
- VM up time??
- VM Cost??

