---
title: Permission Recommendation
parent: CIEM
grand_parent: Notes
nav_order: 1
description: "PRD: compare the permissions cloud identities hold with the ones they exercised across AWS, GCP, Azure, and OCI, and recommend a least-privilege set."
---

# CIEM Permission Optimization

Draft v0.1
{: .label .label-yellow }
Phase 1
{: .label .label-blue }
CIEM · CNAPP
{: .label .label-purple }

A PRD for continuously enforcing least privilege: compare what cloud identities *can* do with what they *actually did*, then recommend the smallest safe permission set.

## On this page
{: .no_toc .text-delta }

- TOC
{:toc}

## 1. Overview

### Product Name

**CIEM Permission Optimization**

### Product Category

Cloud Infrastructure Entitlement Management (CIEM)

### Supported Cloud Providers

* Amazon Web Services (AWS)
* Google Cloud Platform (GCP)
* Microsoft Azure
* Oracle Cloud Infrastructure (OCI)

### Problem Statement

Organizations frequently grant cloud identities significantly more permissions than they actually require.

Over time, users accumulate permissions because of:

* Role changes
* Temporary project access that is never removed
* Broad IAM roles
* Group memberships
* Nested role assignments
* Directly assigned permissions
* Service-specific privileges
* Legacy permissions
* Emergency or temporary elevated access
* Inherited permissions from organization/project/account hierarchy

This creates excessive access and increases the organization's attack surface.

The CIEM Permission Optimization capability will analyze the permissions assigned to an identity and compare them with permissions actually exercised during a configurable historical period.

The system will then recommend a reduced permission set based on observed usage.

At a high level:

**Effective Permission Recommendation = Assigned Permissions − Unused Permissions**

The product should help security and cloud teams answer:

1. **What permissions does this user currently have?**
2. **Which permissions has the user actually used?**
3. **Which permissions have not been used?**
4. **What is the minimum recommended permission set for this user?**
5. **What changes should be made to achieve least privilege?**

## 2. Goals

The primary goal is to enable organizations to continuously enforce the principle of least privilege across multiple cloud providers.

The product should:

* Discover cloud identities and their assigned permissions.
* Calculate the complete effective permission set for each identity.
* Analyze cloud activity logs to determine which permissions have actually been exercised.
* Identify unused and excessive permissions.
* Recommend a least-privilege permission set.
* Provide evidence explaining every recommendation.
* Allow administrators to configure the activity analysis period.
* Support multiple cloud providers through a normalized CIEM permission model.

## 3. Non-Goals

The initial version will not attempt to:

* Automatically revoke permissions without administrator approval.
* Replace the native IAM systems of AWS, Azure, GCP, or OCI.
* Detect application-level authorization outside the cloud IAM layer.
* Guarantee that an unused permission will never be required in the future.
* Analyze permissions inside SaaS products unrelated to the supported cloud providers.
* Automatically redesign an organization's IAM architecture.
* Analyze operating-system-level permissions inside VMs.

Future versions may support automated remediation and Just-in-Time access.

## 4. Target Users

### 4.1 Cloud Security Engineer

Responsible for monitoring excessive permissions and reducing cloud access risks.

Primary needs:

* Identify overprivileged identities.
* Understand why a permission exists.
* Identify dangerous unused permissions.
* Generate least-privilege recommendations.
* Track remediation.

### 4.2 IAM Administrator

Responsible for managing cloud users, roles, groups, and policies.

Primary needs:

* Understand current effective permissions.
* See exactly which role or policy grants each permission.
* Convert recommendations into IAM changes.
* Avoid accidentally removing required permissions.

### 4.3 SOC Analyst

Responsible for investigating suspicious cloud activity.

Primary needs:

* Understand what an identity could potentially access.
* Compare potential permissions with historical behavior.
* Identify privilege escalation paths.
* Investigate unusual permission usage.

### 4.4 Security Leadership / CISO

Primary needs:

* Measure cloud entitlement risk.
* Track excessive privilege reduction.
* Understand organization-wide CIEM posture.
* Monitor least-privilege adoption.

## 5. Key Concepts

### 5.1 Identity

An entity capable of performing actions within a cloud environment.

Examples:

* AWS IAM User
* AWS Identity Center user
* GCP User
* GCP Service Account
* Azure User
* Azure Service Principal
* Azure Managed Identity
* OCI User
* OCI Instance Principal

Although the initial requirement focuses on users, the architecture should support other identities because machine identities often hold significant cloud privileges.

### 5.2 Assigned Permission

A permission that an identity can theoretically exercise based on the organization's IAM configuration.

Assigned permissions may come from:

* Direct role assignment
* Group membership
* Managed policies
* Inline policies
* Inherited roles
* Resource-level policies
* Organization/project/account hierarchy
* Permission sets
* Conditional policies

Example:

```text
s3:GetObject
s3:PutObject
s3:DeleteObject
```

### 5.3 Effective Permission (Not In SCOPE for NOW)

The final permission an identity can exercise after evaluating all applicable IAM policies and controls.

Effective permission may differ from directly assigned permission because of:

* Explicit deny
* Organizational policies
* Permission boundaries
* Resource policies
* Conditional access
* Scope
* Resource restrictions
* Session policies

Example:

```text
Role grants:
s3:*

Permission boundary allows:
s3:GetObject
s3:PutObject

Effective permissions:
s3:GetObject
s3:PutObject
```

The CIEM engine should reason about **effective permissions**, rather than simply listing IAM policies.

### 5.4 Used Permission

A permission inferred from a cloud activity event during the configured analysis period.

Example:

CloudTrail event:

```text
eventName: GetObject
eventSource: s3.amazonaws.com
userIdentity: alice
```

Normalized permission:

```text
s3:GetObject
```

### 5.5 Unused Permission

An effective permission for which no evidence of usage exists during the configured analysis period.

```text
Unused Permissions =
Effective Assigned Permissions
-
Observed Used Permissions
```

Unused permissions should not automatically be treated as safe to remove. They represent candidates for least-privilege remediation.

## 6. User Stories

### Identity Discovery

As a Cloud Security Engineer, I want to see all identities across my connected cloud environments so that I can understand who has access to cloud resources.

### Assigned Permissions

As an IAM Administrator, I want to see all effective permissions assigned to a user so that I understand their actual authorization capabilities.

### Permission Usage

As a Cloud Security Engineer, I want to see which permissions a user exercised during the last X days so that I can differentiate required and unused permissions.

### Least Privilege

As an IAM Administrator, I want recommendations for permissions that can potentially be removed so that I can reduce excessive access.

### Evidence

As a Security Engineer, I want to see the activity events supporting each used permission so that I can trust the recommendation.

## 7. Functional Requirements

### FR-1: Cloud Account Onboarding

The system must allow administrators to connect cloud environments.

Supported initial integrations:

#### AWS

* AWS Organizations
* Individual AWS Accounts

#### GCP

* Organizations
* Folders
* Projects

#### Azure

* Azure Tenant
* Management Groups
* Subscriptions

#### OCI

* OCI Tenancy
* Compartments

The integration should operate using read-only permissions wherever possible.

### FR-2: Identity Discovery

The system must discover identities from each cloud provider.

For every identity, capture:

```text
Identity ID
Identity Name
Identity Type
Cloud Provider
Account / Subscription / Project / Tenancy
Groups
Roles
Policies
Status
Created Date
Last Activity Date
```

Identity types should include:

```text
Human User
Service Account
Role
Service Principal
Managed Identity
Federated Identity
Machine Identity
```

### FR-3: Permission Discovery

The system must determine permissions assigned to each identity.

The system should identify the source of every permission.

Example:

| Permission             | Source         | Assignment    |
| ---------------------- | -------------- | ------------- |
| s3:GetObject           | ReadOnlyAccess | IAM Role      |
| s3:DeleteObject        | S3AdminPolicy  | IAM Group     |
| ec2:TerminateInstances | AdminPolicy    | Direct Policy |

The system must support permissions inherited through groups and roles.

### FR-4: Effective Permission Calculation

The system must calculate the effective permission set for each identity.

The calculation should consider provider-specific IAM behavior.

#### AWS

Potential inputs include:

* IAM policies
* IAM groups
* IAM roles
* Managed policies
* Inline policies
* Permission boundaries
* Service Control Policies
* Resource policies
* Session policies
* Explicit deny rules

#### Azure

Potential inputs include:

* Azure RBAC assignments
* Custom roles
* Built-in roles
* Management group inheritance
* Subscription roles
* Resource group roles
* Resource-level assignments
* Deny assignments
* Conditional access where relevant

#### GCP

Potential inputs include:

* IAM policies
* Predefined roles
* Custom roles
* Basic roles
* Organization inheritance
* Folder inheritance
* Project-level IAM
* Resource-level IAM
* IAM Conditions
* Organization Policies where relevant

#### OCI

Potential inputs include:

* Users
* Groups
* Policies
* Compartments
* Dynamic groups
* Identity domains
* Policy inheritance

### FR-5: Activity Log Collection

The system must collect activity data from native cloud audit systems.

#### AWS

Primary sources:

```text
AWS CloudTrail
CloudTrail Lake where configured
```

#### GCP

Primary sources:

```text
Cloud Audit Logs
Admin Activity
Data Access Logs
System Event Logs
```

#### Azure

Primary sources:

```text
Azure Activity Log
Microsoft Entra audit/sign-in telemetry where required
Resource-specific diagnostic logs where applicable
```

#### OCI

Primary sources:

```text
OCI Audit
```

The ingestion pipeline should normalize events into a common CIEM activity schema.

### FR-6: Configurable Analysis Window (Tenant Specific)

Administrators must be able to select the historical usage period.

Suggested options:

```text
7 days
30 days
60 days
90 days
180 days
365 days
Custom
```

Recommended default:

```text
90 days
```

The selected period must be displayed with every recommendation.

Example:

> Permission `s3:DeleteBucket` has not been observed between May 20 and August 18.

### FR-7: Activity-to-Permission Mapping

The system must map cloud audit events to IAM permissions.

Example:

```text
CloudTrail Event
eventSource = s3.amazonaws.com
eventName = DeleteObject
```

Maps to:

```text
s3:DeleteObject
```

Normalized internal representation:

```json
{
  "provider": "AWS",
  "service": "S3",
  "action": "DeleteObject",
  "permission": "s3:DeleteObject"
}
```

Provider-specific mapping libraries should be maintained by the platform.

### FR-8: Permission Usage Analysis

For each identity, classify permissions into:

```text
Used
Unused
Unknown
```

#### Used

Evidence exists that the identity exercised the permission.

#### Unused

The permission exists but no activity was observed during the selected period.

#### Unknown

The system cannot reliably determine usage.

Potential reasons:

* Audit logging disabled
* Data-access logging unavailable
* Unsupported cloud service
* Insufficient log retention
* Incomplete telemetry
* Permission cannot be directly mapped to an API operation

Unknown permissions must never automatically be treated as unused.

### FR-9: Effective Permission Recommendation

The system must produce a recommended permission set.

Conceptually:

```text
Recommended Permissions =
Used Permissions
+
Required Dependency Permissions
+
Protected Permissions
```

And:

```text
Removal Candidates =
Effective Permissions
-
Recommended Permissions
```

Example:

#### Assigned

```text
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:DeleteBucket
s3:CreateBucket
```

#### Used during last 90 days

```text
s3:GetObject
s3:PutObject
```

#### Recommended

```text
KEEP:
s3:GetObject
s3:PutObject

REMOVE CANDIDATES:
s3:DeleteObject
s3:DeleteBucket
s3:CreateBucket
```

### FR-10: Permission Recommendation Confidence

Each recommendation should contain a confidence level.

Example:

```text
High
Medium
Low
```

Factors influencing confidence:

* Log coverage
* Analysis duration
* Number of observed activities
* Mapping confidence
* Historical consistency
* Identity activity frequency

Example:

```text
Unused Permission:
ec2:TerminateInstances

Last observed:
Never within available 180-day history

Confidence:
High
```

### FR-11: Permission Risk Classification

Permissions should be classified by security impact.

Example categories:

```text
Read
Write
Delete
Administrative
IAM Modification
Privilege Escalation
Credential Management
Data Exfiltration
Security Control Modification
Billing
Network Modification
Encryption / KMS
```

Example high-risk permissions:

```text
iam:CreateUser
iam:AttachUserPolicy
iam:PassRole
kms:Decrypt
s3:DeleteBucket
ec2:TerminateInstances
```

Risk information should help administrators prioritize unused permissions.

### FR-12: Identity Risk Score

Each identity should receive an entitlement risk score.

Possible scoring dimensions:

```text
Number of unused permissions
Number of privileged permissions
Number of unused privileged permissions
Administrative roles
Sensitive resource access
Cross-account access
Dormant identity
Publicly exposed credentials
Privilege escalation possibilities
```

Example:

```text
Identity: john@example.com

Risk Score: 87 / 100

Critical Findings:
12 unused administrative permissions
3 privilege-escalation permissions
1 unused credential-management permission
```

### FR-13: Permission Detail View

Administrators must be able to inspect a permission.

Example:

```text
Permission
s3:DeleteBucket

Identity
john@example.com

Cloud
AWS

Account
Production

Granted Through
S3FullAccess

Assignment
Engineering-Admins group

Last Used
Not observed

Analysis Window
180 days

Risk
High

Recommendation
Consider removing

Confidence
High
```

### FR-14: Usage Evidence

For permissions classified as used, the system should provide supporting activity.

Example:

```text
Permission:
s3:GetObject

Observed:
147 times

First observed:
2026-05-20

Last observed:
2026-08-17

Resources:
prod-customer-data
prod-reporting
```

Users should be able to drill into associated audit events.

### FR-15: Recommendation Explanation

Every recommendation must explain why it exists.

Example:

```text
Recommendation

Remove s3:DeleteBucket from john@example.com.

Reason:

The identity has this permission through the
"S3FullAccess" policy.

No DeleteBucket activity has been observed during
the last 180 days.

CloudTrail coverage for the account is complete.

Permission risk classification: High.

Recommendation confidence: High.
```

### FR-16: Recommended Role / Policy Generation

Where technically feasible, the product should create a suggested least-privilege policy.

Example AWS output:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::example-bucket/*"
      ]
    }
  ]
}
```

Equivalent recommendation artifacts may include:

* AWS IAM policy
* GCP custom role
* Azure custom RBAC role
* OCI policy statement

Generated policies should be recommendations only in the initial release.

### FR-17: Resource Scope Analysis

Permissions should be analyzed together with their resource scope.

Example:

```text
Assigned:
s3:GetObject on *

Observed:
s3:GetObject only on arn:aws:s3:::finance-reports/*
```

Recommendation:

```text
Change:

s3:GetObject on *

To:

s3:GetObject on arn:aws:s3:::finance-reports/*
```

Least privilege should therefore cover both:

```text
Action reduction
AND
Resource scope reduction
```

### FR-18: Wildcard Permission Expansion

The engine must analyze wildcard permissions.

Example:

```text
s3:*
```

should be expanded into the provider's known permission catalog before performing usage analysis.

Similarly:

```text
ec2:Describe*
```

must be interpreted as the corresponding matching EC2 permissions.

### FR-19: Group-Level Recommendations

If excessive permissions are inherited through a group, the system should indicate whether modifying the group would impact other identities.

Example:

```text
User:
alice

Unused permission:
s3:DeleteBucket

Granted by:
EngineeringAdmins

Group members:
42

Recommendation:
Do not modify the shared role directly.

Consider moving Alice to a lower-privilege group.
```

### FR-20: Dashboard

The main CIEM dashboard should show:

```text
Total identities
Privileged identities
Overprivileged identities
Dormant identities
Total permissions
Unused permissions
Unused high-risk permissions
Least-privilege recommendations
```

Example:

```text
12,432 Identities

3,821 Overprivileged Identities

74% of granted permissions unused

487 High-Risk Unused Permissions

1,247 Least-Privilege Recommendations
```

## 8. Primary Product Screens

### 8.1 CIEM Overview

Widgets:

* Total identities
* Overprivileged identities
* Privileged identities
* Dormant identities
* Unused permission percentage
* High-risk permission exposure
* Cloud-provider breakdown
* Top risky identities
* Top risky permissions

### 8.2 Identities

Example table:

| Identity     | Cloud | Assigned | Used | Unused | Risk     | Last Active |
| ------------ | ----- | -------: | ---: | -----: | -------- | ----------- |
| Alice        | AWS   |      487 |   42 |    445 | Critical | Today       |
| Bob          | Azure |      122 |   31 |     91 | High     | 3 days ago  |
| Analytics-SA | GCP   |       74 |   62 |     12 | Medium   | Today       |

Filters:

* Cloud
* Account
* Identity type
* Risk
* Permission category
* Activity
* Recommendation status

### 8.3 Identity Detail

Header:

```text
Alice
alice@example.com

AWS / Production Account
```

Summary:

```text
Assigned Permissions: 487
Used Permissions: 42
Unused Permissions: 445
Unused %: 91%
Risk Score: Critical
```

Tabs:

```text
Overview
Assigned Permissions
Used Permissions
Unused Permissions
Roles & Policies
Activity
Recommendations
```

### 8.4 Permission Recommendation

Example:

```text
Identity
Alice

Current Role
AdministratorAccess

Observed Activity
42 permissions

Current Permission Count
487

Recommended Permission Count
56

Potential Reduction
88.5%
```

Action:

```text
View Recommended Policy
Export Recommendation
Mark as Accepted Risk
Dismiss
Create Remediation Ticket
```

## 9. Data Model

A normalized cross-cloud model should be used.

### Identity

```text
identity_id
provider_identity_id
identity_name
identity_type
provider
tenant/account/project
status
created_at
last_activity_at
```

### Permission

```text
permission_id
provider
service
action
resource
risk_level
risk_category
```

### Entitlement

```text
identity_id
permission_id
source_type
source_id
resource_scope
conditions
effective_status
```

### Permission Usage

```text
identity_id
permission_id
event_count
first_observed
last_observed
resources_used
analysis_window
```

### Recommendation

```text
recommendation_id
identity_id
permission_id
recommendation_type
risk
confidence
reason
status
created_at
```

## 10. Architecture

Suggested high-level architecture:

```text
                 +--------------------+
                 |    AWS Connector   |
                 +--------------------+

                 +--------------------+
                 |    GCP Connector   |
                 +--------------------+

Cloud IAM -----> +--------------------+
                 |   Azure Connector  |
                 +--------------------+

                 +--------------------+
                 |    OCI Connector   |
                 +--------------------+

                          |
                          v

                 +--------------------+
                 | Identity & IAM     |
                 | Normalization      |
                 +--------------------+

                          |
                          v

                 +--------------------+
                 | Effective          |
                 | Permission Engine  |
                 +--------------------+

                          |
                          |
Cloud Logs ------------------------------+
                          |              |
                          v              v

                 +--------------------+
                 | Activity           |
                 | Normalization      |
                 +--------------------+

                          |
                          v

                 +--------------------+
                 | Permission Usage   |
                 | Correlation Engine |
                 +--------------------+

                          |
                          v

                 +--------------------+
                 | Recommendation     |
                 | Engine             |
                 +--------------------+

                          |
                          v

                 +--------------------+
                 | Risk & Confidence  |
                 | Engine             |
                 +--------------------+

                          |
                          v

                 +--------------------+
                 | CIEM API / UI      |
                 +--------------------+
```

## 11. Recommendation Engine

The core algorithm can conceptually operate as follows.

### Step 1 — Resolve effective permissions

```text
EffectivePermissions(identity)
```

### Step 2 — Collect activity

```text
Events(identity, analysis_window)
```

### Step 3 — Map events to permissions

```text
UsedPermissions =
MapEventsToPermissions(events)
```

### Step 4 — Calculate unused permissions

```text
UnusedPermissions =
EffectivePermissions
-
UsedPermissions
```

### Step 5 — Exclude uncertain recommendations

```text
CandidatePermissions =
UnusedPermissions
-
UnknownPermissions
-
ProtectedPermissions
```

### Step 6 — Calculate risk

```text
Risk(permission)
```

### Step 7 — Calculate confidence

```text
Confidence(
 log_coverage,
 observation_period,
 identity_activity,
 mapping_quality
)
```

### Step 8 — Generate recommendation

```text
Recommendation(
 identity,
 permission,
 source,
 risk,
 confidence
)
```

## 12. Important Safety Guardrails

Purely usage-based permission removal can cause production outages.

The recommendation engine must therefore include safety mechanisms.

### 12.1 Minimum Observation Window

Administrators should be warned when the observation period is too short.

Example:

```text
Only 7 days of activity history is available.

This identity may execute monthly or quarterly operations.

Recommendation confidence: Low.
```

### 12.2 Rare Operations

Some permissions are legitimately used infrequently.

Examples:

```text
Disaster recovery
Certificate rotation
Quarterly reporting
Database restore
Key rotation
Incident response
Deployment rollback
Account recovery
```

The product should allow permissions to be marked:

```text
Required but Rarely Used
```

### 12.3 Incomplete Log Coverage

If logging is incomplete:

```text
Do NOT classify permission as confidently unused.
```

Instead:

```text
Usage Status: Unknown

Reason:
Required audit log source is not enabled.
```

### 12.4 Break-Glass Accounts

Emergency or break-glass identities should be flagged and excluded from standard recommendations where configured.

### 12.5 Protected Permissions

Administrators should be able to create policies such as:

```text
Never recommend removal of:
kms:Decrypt

for identities tagged:
Team = DisasterRecovery
```

## 13. Recommendation Types

The system should support multiple least-privilege recommendation types.

### Remove Permission

```text
Remove unused action.
```

### Replace Role

```text
Administrator
→
ReadOnly
```

### Reduce Resource Scope

```text
s3:GetObject on *
→
s3:GetObject on finance-bucket/*
```

### Reduce Role Scope

```text
Subscription Owner
→
Resource Group Contributor
```

### Remove Group Membership

```text
Remove user from CloudAdmins.
```

### Replace Managed Role With Custom Role

```text
AWS PowerUserAccess
→
Custom application operator policy
```

### Remove Dormant Access

```text
Identity has not been active for 180 days.
```

## 14. Recommendation Lifecycle

Recommendations should have a workflow state.

```text
Open
Under Review
Approved
Remediation Planned
Remediated
Dismissed
Accepted Risk
Reopened
```

Metadata should include:

```text
Created Date
Owner
Reviewer
Reason
Remediation Date
Ticket Reference
```

## 15. Integrations

Future integrations may include:

```text
Jira
ServiceNow
Slack
Microsoft Teams
SIEM
SOAR
Identity Governance systems
```

Potential workflows:

```text
CIEM Finding
      ↓
Create ServiceNow Ticket
      ↓
IAM Administrator Approval
      ↓
Permission Change
      ↓
CIEM Verification
      ↓
Finding Closed
```

## 16. Reporting

Reports should include:

### Least Privilege Coverage

```text
% of identities operating within recommended privilege levels
```

### Permission Utilization

```text
Used Permissions / Assigned Permissions
```

### Excessive Permission Rate

```text
Unused Permissions / Effective Permissions
```

### Privileged Permission Exposure

```text
Unused high-risk permissions
```

### Remediation Progress

```text
Recommendations generated
Recommendations remediated
Recommendations accepted as risk
```

## 17. Success Metrics

Primary product KPIs:

### Permission Reduction

```text
% reduction in excessive permissions
```

### Privileged Permission Reduction

```text
% reduction in unused high-risk permissions
```

### Identity Coverage

```text
% of cloud identities analyzed
```

### Recommendation Confidence

```text
% of recommendations classified as High Confidence
```

### Recommendation Adoption

```text
Approved recommendations /
Generated recommendations
```

### Time to Remediation

```text
Average time from recommendation creation
to permission remediation
```

## 18. MVP Scope

The MVP should focus on visibility and recommendations rather than automatic remediation.

### MVP Capabilities

* Connect AWS, Azure, GCP, and OCI accounts.
* Discover human identities.
* Discover roles, groups, and policy assignments.
* Calculate assigned/effective permissions.
* Ingest native cloud audit logs.
* Configure analysis period.
* Map activity events to IAM permissions.
* Display used permissions.
* Display unused permissions.
* Show permission source.
* Generate least-privilege recommendations.
* Rank recommendations by risk.
* Show recommendation confidence.
* Provide evidence supporting recommendations.
* Export recommendations.

## 19. Phase 2

Potential Phase 2 capabilities:

* Service account analysis
* Managed identities
* Workload identities
* Resource-level privilege optimization
* Group-level role recommendations
* Custom IAM policy generation
* Recommendation approval workflow
* Jira integration
* ServiceNow integration
* Risk exception management

## 20. Phase 3

Potential advanced CIEM capabilities:

* Automated permission remediation
* Approval-based remediation
* Just-in-Time access
* Just-Enough-Access
* Privilege escalation graph
* Identity attack paths
* Cross-cloud identity correlation
* IAM anomaly detection
* Permission usage prediction
* Suggested role clustering

Example:

```text
23 developers currently have 17 different
permission combinations.

CIEM recommendation:

Create standardized role:

"ProductionReadOnlyDeveloper"

and migrate 19 identities to the role.
```

## 21. Key Technical Challenges

### Permission Normalization

Every cloud provider uses a different authorization model.

A normalized model should allow comparison such as:

```text
Provider
Service
Action
Resource
Effect
Condition
Source
```

without hiding cloud-specific behavior.

### Event-to-Permission Mapping

Not every audit event maps cleanly to exactly one permission.

The platform will require a continuously maintained permission mapping catalog.

### IAM Evaluation Complexity

Determining what a user **can actually do** is more difficult than simply listing attached roles.

The effective permission engine is therefore one of the critical components of the system.

### Missing Telemetry

Certain permission usage may not appear unless specific cloud logging options are enabled.

The product must distinguish:

```text
Unused
```

from:

```text
Unable to determine usage
```

to prevent unsafe recommendations.

## 22. Example End-to-End Scenario

Consider:

```text
User:
alice@example.com

Cloud:
AWS

Role:
PowerUserAccess

Effective Permissions:
1,250
```

CIEM analyzes 180 days of CloudTrail activity.

Observed:

```text
67 unique permissions used.
```

The system determines:

```text
Effective Permissions: 1,250

Observed Permissions: 67

Unknown / Insufficient Telemetry: 15

Removal Candidates: 1,168
```

CIEM identifies among the unused permissions:

```text
iam:CreateAccessKey
iam:PassRole
lambda:DeleteFunction
s3:DeleteBucket
kms:ScheduleKeyDeletion
```

Risk engine determines:

```text
5 Critical
18 High
192 Medium
953 Low
```

Recommendation:

```text
Replace PowerUserAccess with
CIEM-Generated-DeveloperRole.
```

Proposed role contains:

```text
81 permissions
```

consisting of:

```text
67 observed permissions
+
14 dependency/protected permissions
```

Result:

```text
Permission reduction:
1,250 → 81

Reduction:
93.5%
```

The user can inspect each removed permission, its original entitlement source, last-observed usage, log coverage, associated resource scope, risk, and recommendation confidence before taking action.

## 23. Core Product Principle

The product should **not** simply answer:

> "Which permissions haven't appeared in the logs?"

It should answer the more security-relevant question:

{: .important }
> **"Based on this identity's current entitlements, observed behavior, resource scope, telemetry coverage, permission risk, and organizational policy, what is the safest least-privilege access model we can recommend?"**

That distinction should guide the CIEM Permission Optimization architecture and product experience.

<nav class="doc-pager" aria-label="Document navigation">
  <span></span>
  <a class="doc-pager-link is-next" href="../02-ciem-permission/">
    <span class="doc-pager-label">Next</span>
    <span class="doc-pager-title">Permission Recommendation MVP</span>
  </a>
</nav>
