---
title: Cloud Account Naming
parent: Notes
nav_order: 9
description: "CLI commands to fetch the human-readable account/subscription/project name per cloud (AWS, Azure, GCP, OCI)."
---

# Cloud Account CMD to get Account Name

## AWS 
cmd - aws account get-account-information
output - (AccountName)
```json
{
    "AccountCreatedDate": "2022-12-26T06:09:03+00:00",
    "AccountId": "956994857092",
    "AccountName": "AccuKnox-dev"
}
```

## Azure
cmd - az account show --subscription f25ebac7-f91b-49e3-b9cb-aa578e0e5342
output - (name)
```json
{
  "environmentName": "AzureCloud",
  "homeTenantId": "825a7bf3-be45-47e9-86d5-565d24b0a7fb",
  "id": "f25ebac7-f91b-49e3-b9cb-aa578e0e5342",
  "isDefault": true,
  "managedByTenants": [
    {
      "tenantId": "3d64034d-3c3e-4959-b019-f15558be8a4e"
    }
  ],
  "name": "AZ-Sub-1",
  "state": "Enabled",
  "tenantDefaultDomain": "ayushaggarwal1136gmail.onmicrosoft.com",
  "tenantDisplayName": "Default Directory",
  "tenantId": "825a7bf3-be45-47e9-86d5-565d24b0a7fb",
  "user": {
    "name": "ayushaggarwal1136_gmail.com#EXT#@ayushaggarwal1136gmail.onmicrosoft.com",
    "type": "user"
  }
}
```

## GCP
cmd - gcloud projects describe shaped-infusion-402417 --format=json
output - (name)
```json
{
  "createTime": "2023-10-18T17:18:03.989398Z",
  "lifecycleState": "ACTIVE",
  "name": "shaped-infusion",
  "parent": {
    "id": "955809990560",
    "type": "organization"
  },
  "projectId": "shaped-infusion-402417",
  "projectNumber": "319116921477"
}
```

## OCI
cmd1 - oci iam compartment get --compartment-id ocid1.compartment.oc1..aaaaaaaadumul7gp7lyo57rqmuj7hyx4xejivcdczfyx7ajg3lp3skwlnolq --query 'data.name' --raw-output
output1 - (name)


cmd2 - oci iam compartment get --compartment-id ocid1.compartment.oc1..aaaaaaaadumul7gp7lyo57rqmuj7hyx4xejivcdczfyx7ajg3lp3skwlnolq
output2 - (data.name)
```json
{
  "data": {
    "compartment-id": "ocid1.tenancy.oc1..aaaaaaaa4radaaoyfqge6byfykniwjnofrrbq2lyruzlbfeyv6rkysu6sbxa",
    "defined-tags": {
      "Oracle-Tags": {
        "CreatedBy": "oracleidentitycloudservice/muhammad.sohaib@fidelityunited.ae",
        "CreatedOn": "2022-04-11T06:24:08.253Z"
      }
    },
    "description": "dr",
    "freeform-tags": {},
    "id": "ocid1.compartment.oc1..aaaaaaaadumul7gp7lyo57rqmuj7hyx4xejivcdczfyx7ajg3lp3skwlnolq",
    "inactive-status": null,
    "is-accessible": true,
    "lifecycle-state": "ACTIVE",
    "name": "DR",
    "time-created": "2022-04-11T06:24:08.374000+00:00"
  },
  "etag": "0eda98a2cbeb783215d9509829ab44f1894f58c3"
}
```


# AccuKnox Celery Task to run
python3 manage.py tenant_command shell --schema=knoxaccuknoxtech1774589033

```python
from soarcast.playbook.tasks import check_daily_cloud_active_status
check_daily_cloud_active_status.delay()
```

```
from soarcast.playbook.tasks import check_daily_cloud_active_status
check_daily_cloud_active_status()
```