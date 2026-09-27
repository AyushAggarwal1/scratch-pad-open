---
title: Prowler
parent: Security Tools Cmds
grand_parent: Cmds
nav_order: 5
description: "Per-cloud Prowler identity-access scan commands (AWS, Azure, GCP, OCI) with OCSF JSON output."
---
{% raw %}

# Prowler

**aws**
- prowler aws --category identity-access --output-formats json-ocsf --output-filename aws-pw-identity.json --output-directory .

**azure**
- prowler azure --sp-env-auth --category identity-access --subscription-id {{subs-id}} --output-formats json-ocsf --output-filename azure-pw-identity.json --output-directory .

export AZURE_CLIENT_ID={{client_id}}
export AZURE_TENANT_ID={{tenant_id}}
export AZURE_CLIENT_SECRET={{secret}}

**gcp**
- prowler gcp --category identity-access --credentials-file {{file_path}} --project-id {{project_id}} --output-formats json-ocsf --output-filename gcp-pw-identity.json --output-directory .

**oci**
- prowler oci --category identity-access --oci-config-file {{file_path}} --compartment-id {{compartment_id}} --output-formats json-ocsf --output-filename oci-pw-identity.json --output-directory .
{% endraw %}
