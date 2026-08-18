---
title: Notes & Use Cases
parent: Rule Engine for Assets
grand_parent: Notes
nav_order: 2
description: "Working notes and use cases for asset-scoped rules — the earlier, rougher pass that fed the backend requirements doc."
---

## Rule Engine for Assets
When Rule Engine Triggers then RE extracts Findings ID and then perform Actions

### Current Limitations
1. User is not able to notifiy in context of assets

### Requirements
1. Add `Is New` for Assets
2. Craete Filter-Fields API for assets
3. Rule Engine to Run in Context of Assets
4. User Creates set of Condiditons
5. Actions:
    3.1 Create Ticket
    3.2 Send to Notification
6. Ticket Config for Assets

### Use-Cases
1. Asset Type = Unmanaged AI Assets && Add `Is_New` field for Assets -> Send Notification
    1.1 Asset `Not Find In`
2. If `Public` tag is added to an Asset
3. Send Alert if `is_eol` True
4. If Asset `Is_New` then finding is auto considered as `is_new`
5. Assets with Critical Finidngs
6. If Last_Seen is > 30 Days 
