---
title: Oracle Cloud Setup
parent: Notes
nav_order: 17
description: "OCI IAM policy statements for onboarding a tenancy under the CSPM and CIEM policy sets."
---

# Oracle Cloud Onboarding

- Create a User in Domain
- Create a Group and Assign to User
- Create the policy with below Policy

## Oracle CSPM Policy
Allow group {{group_name}} to read all-resources in tenancy
Allow group {{group_name}} to inspect all-resources in tenancy

Allow group 'Default'/'{{group_name}}' to inspect all-resources in tenancy
Allow group '{{domain_name}}'/'{{group_name}}' to inspect all-resources in tenancy

## Oracle CIEM Policy
Allow group 'Default'/'ciem-accuknox' to read all-resources in tenancy
Allow group 'Default'/'ciem-accuknox' to inspect all-resources in tenancy

Allow group 'Default'/'ciem-accuknox' to read audit-events in tenancy
Allow group 'Default'/'ciem-accuknox' to read users in tenancy

Allow group 'Default'/'ciem-accuknox' to inspect groups in tenancy
Allow group 'Default'/'ciem-accuknox' to inspect dynamic-groups in tenancy

Allow group 'Default'/'ciem-accuknox' to inspect policies in tenancy
Allow group 'Default'/'ciem-accuknox' to inspect compartments in tenancy