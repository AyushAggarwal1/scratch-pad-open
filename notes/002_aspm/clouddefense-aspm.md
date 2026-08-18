---
title: CloudDefense Comparison
parent: ASPM
grand_parent: Notes
nav_order: 3
description: "A feature-by-feature look at CloudDefense's ASPM offering against AccuKnox, and the gaps worth exploiting."
---

CloudDefense ASPM
- Onboard Source Code Repo from UI                  :       AccuKnox WIP
- Co-Relation Scan of Code to DAST                  :            --
- Vulnerabilty Context (Impact - How to Exploit).   :       This will be achievable by AI- SAST
- Vulnerabilty Graph                                :       CD is using OpenAI (Costly), We can deploy a local Model
- Checks Managment                                  :       WIP for CSPM
- Mobo App Scanning (APK Only)                      :       AccuKnox can build a collector using MOB-SF

CD Feature Lack
- Scan 1 Banch Per Repo
- No Auth for SAST with DAST
- Co-Relate SAST with DAST
- No Option to Select Scan Type

Actions Items
- Deploy a LLM/ AI Service on Proxmox Server that will 
    - Gives [Vulnerabilty Context like Impact - How to Exploit - Remediation wrt Code]
    - Creates a Graph of each finding from source to emit
