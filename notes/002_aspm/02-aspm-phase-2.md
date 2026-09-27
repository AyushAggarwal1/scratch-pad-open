---
title: ASPM Phase 2
parent: ASPM
grand_parent: Notes
nav_order: 2
description: "Phase 2 deliverables for ASPM — assets view, PR-based scanning, API discovery, and the asset data model."
---

# ASPM Phase 2


**Phase-2**
- ASPM Assets View
- Bitbucket OnPrem (Enterprise)
- Build Location as Repo Redirection URL
- Scan Public Repos without App/ Token
- Notion to Onboard using Github Tags
- DAST 
- SAST Enrichment
  - CVE's
  - CWE's
- Mobile APK Scanning
- AI Based Remediation
- PR based Scanning
- API Discovery

**Functional Reqs**
- Group by Namespace (Gitlab/ Bitbucket)

**Asset Types**
Organisation (Organistion/ Users/ Workspace/) 
-> Group (Project/ Group) 
    -> Repo
      -> Branches
      -> PR



organisatio_name          provider          connector_name                      total_repo_count

accuknox                   github              ak_github                                2

  repos_name              totoal_branches/ prs        total_vulnerabilities        last_seen
    repo1                         3                      X High Y Medium             18 Aug
        
    Branches
        dev                                             X High Y Medium             18 Aug
        pre-stage                                       X High Y Medium             18 Aug
        ayush-pre-stage (#PR_No)

    repo2




AyushAggarwal1             gitlab                 ayush_gitlab                       2

  repos_name              totoal_branches/ prs        total_vulnerabilities        last_seen
    repo1                         3                      X High Y Medium             18 Aug
        
    Branches
        dev                                             X High Y Medium             18 Aug
        pre-stage                                       X High Y Medium             18 Aug
        ayush-pre-stage (#PR_No)

    repo2



 