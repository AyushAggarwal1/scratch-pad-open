---
title: ASPM Phase 1
parent: ASPM
grand_parent: Notes
nav_order: 1
description: "Phase 1 deliverables for ASPM — supported SCMs and scan types, CLI/action workflow, AI-SAST, and redirection rules."
---

# ASPM Phase 1


**ASPM**
Product Owner - Ayush Aggarwal

**Phase-1 Deliverables**
Supported SCM with Branch and Scan Type Selection
- Github (Columbia, Compunel, Primanal, AWR)
  - Cloud                        
  - OnPrem (Enterprise)          

- Gitlab (Columbia)
  - Cloud
  - OnPrem (Enterprise)

- BitBucket (Compunel, Nomics)
  - Cloud                         

**Supported Scan Types**
- SAST                : OpenGrep (Enable AI-SAST Per Repo Based)
- SCA                 : Trivy
- Secret              : Gitleaks/ TruffleHog
- IAC with Frameworks : CheckOV
- SBOM - (trivy fs "path" --format cyclonedx --output sbom.json)           
  - Generation 
  - Upload BOM
  - SBOM Vulnerabilities
- IDE Integration
- Event-Trail


**New ASPM CLI/ Action/ Workflow**
for Github, Gitlab, Bitbucket, Azure Devops
- Consolidate All type of Scanners in Single Action
- CLI options Ability to Scan only New Changes for New PR's/ Commits


**Phase -1 Action Items**
Story - https://accu-knox.atlassian.net/browse/CNAPP-26532
Dev 1 (s)
    - Support for Github, Gitlab, Bitbucket (Cloud/ Enterprise)
    - Phase 1 Support Scan Types
        - SAST                : OpenGrep (Enable AI-SAST Per Repo Based)
        - SCA                 : Trivy
        - Secret              : Gitleaks/ TruffleHog
        - IAC with Frameworks : CheckOV
        - ML Static Scan      : Model Scan
        - API Discovery       : code2api

Dev 2 (ab)
    - Onboarding UI
    - Support for Github, Gitlab, Bitbucket (Cloud/ Enterprise)

Dev 3 (v)
    - AI SAST Playbook
    - Quality Gates

Dev 4 (i)
    - CLI to Support Phase 1 Support Scan Types
        - SAST                : OpenGrep (Enable AI-SAST Per Repo Based)
        - SCA                 : Trivy
        - Secret              : Gitleaks/ TruffleHog
        - IAC with Frameworks : CheckOV
        - ML Static Scan      : Model Scan
        - API Discovery       : code2api
    
    - Abiliy to Scan only New Changes in CLI via a flag

Dev 5 (vi)
    - Unified Action for All Scanner
        - SAST                : OpenGrep (Enable AI-SAST Per Repo Based)
        - SCA                 : Trivy
        - Secret              : Gitleaks/ TruffleHog
        - IAC with Frameworks : CheckOV
        - ML Static Scan      : Model Scan
        - API Discovery       : code2api
    - Github, Gitlab, Bitbucket, Azure Devops, Jenkins

- Help Document for ASPM          : ?


**AI-SAST**
- Owner - Eshrath
- Current Capabilities
  - Severity
  - Verdit (TP/ FP)
  - Reason

- Extended Capabilities for NEW ASPM
  - Business Impact
  - Rationale
  - Exploitability
  - Remediation

- Code Assure [Brain of AI-SAST]

```JSON
{
  "model": {
    "provider": "openai-compatible",
    "name": "your-model-name",
    "api_base": "http://localhost:5000",
    "api_key": "$YOUR_API_KEY_ENV_VAR",
    "tool_calling": true
  },
  "concurrency": 4,
  "stage_timeout": 120,
  "finding_timeout": 300,
  "finding_policy": {
    "best_practice_is_tp": true,
    "informational_detection_is_tp": true,
    "audit_rule_is_tp": true
  }
}
```

**Redirection**
SAST
    - Asset Name
    - Branch
    - Severity

IAC (branch in asset name)
    - Asset Name
    - Severity

SCA (branch in asset name)
    - Asset Name
    - Severity

Secret (branch in asset name)
    - Asset Name

All Scanner