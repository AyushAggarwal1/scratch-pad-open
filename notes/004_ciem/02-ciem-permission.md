---
title: Permission Recommendation MVP
parent: CIEM
grand_parent: Notes
nav_order: 2
description: "PRD for the MVP slice: for a selected cloud user, list assigned permissions, analyze X days of audit logs, and recommend keep or remove."
---

# CIEM Permission Recommendation — MVP

Draft v0.1
{: .label .label-yellow }
Phase 2
{: .label .label-blue }
CIEM · CNAPP
{: .label .label-purple }

The deliberately small first slice of [Permission Optimization](01-ciem-permission.md): one selected user, X days of audit logs, and keep-or-remove recommendations.

## On this page
{: .no_toc .text-delta }

- TOC
{:toc}

## 1. Product Overview

### Product Name

**CIEM Permission Recommendation**

### Objective

For a selected cloud user:

1. Identify all permissions assigned to the user.
2. Identify how each permission is assigned:

   * Direct policy
   * Group
   * Role
   * Inherited policy
3. Check cloud audit logs for the last **X days**.
4. Identify which permissions were actually used.
5. Compare assigned permissions with used permissions.
6. Recommend removing permissions that were not used.

## 2. Problem Statement

Cloud users are often assigned more permissions than they actually require.

Permissions may be granted through:

```text
User
 ├── Direct Policy
 ├── Group
 ├── Role
 └── Inherited Policy
```

Over time, users may retain permissions they no longer use.

The product should identify these unused permissions and recommend a smaller permission set based on actual activity.

## 3. Core Product Flow

```text
User
 │
 ▼
Find Assigned Permissions
 │
 ├── Direct Policies
 ├── Groups
 ├── Roles
 └── Inherited Policies
 │
 ▼
Assigned Permission List
 │
 ▼
Read Audit Logs for Last X Days
 │
 ▼
Identify Used Permissions
 │
 ▼
Compare
 │
 ├── Used Permission
 │       ↓
 │      KEEP
 │
 └── Unused Permission
         ↓
       REMOVE
```

## 4. Core Logic

```text
Assigned Permissions
=
All permissions available to the user
through Group / Role / Policy / Direct Assignment
```

```text
Used Permissions
=
Permissions observed in audit logs
during the selected time period
```

```text
Unused Permissions
=
Assigned Permissions - Used Permissions
```

```text
Recommended Permissions
=
Used Permissions
```

```text
Permissions Recommended for Removal
=
Assigned Permissions - Used Permissions
```

## 5. Supported Cloud Providers

Initial product should support:

* AWS
* GCP
* Microsoft Azure
* Oracle Cloud Infrastructure

Each cloud provider will have:

1. Permission Collector
2. Log Collector
3. Log-to-Permission Mapper

The recommendation logic remains common across all providers.

## 6. Functional Requirements

### FR-1: Select User

User should be able to select a cloud identity.

Example:

```text
Cloud: AWS
Account: Production
User: alice
```

### FR-2: Discover Assigned Permissions

The system should identify all permissions available to the selected user.

Permissions may come through:

* Direct policy
* Group membership
* Role
* Managed policy
* Inline policy
* Inherited assignment

Example:

```text
User: Alice

Role:
DeveloperRole

Permissions:
s3:GetObject
s3:PutObject
s3:DeleteObject
ec2:StartInstances
ec2:StopInstances
```

### FR-3: Show Permission Source

For every permission, show how the user received it.

Example:

| Permission         | Assigned Via | Source        |
| ------------------ | ------------ | ------------- |
| s3:GetObject       | Role         | DeveloperRole |
| s3:PutObject       | Role         | DeveloperRole |
| s3:DeleteObject    | Group        | AdminGroup    |
| ec2:StartInstances | Policy       | EC2Developer  |
| ec2:StopInstances  | Policy       | EC2Developer  |

## 7. Log Analysis

The system should analyze cloud activity logs.

### AWS

```text
CloudTrail
```

### GCP

```text
Cloud Audit Logs
```

### Azure

```text
Azure Activity Logs / relevant audit logs
```

### OCI

```text
OCI Audit Logs
```

## 8. Analysis Period

User should be able to select:

```text
Last 7 Days
Last 30 Days
Last 60 Days
Last 90 Days
Last 180 Days
Custom
```

Default:

```text
90 Days
```

## 9. Identify Used Permissions

The system should read audit events belonging to the selected user.

Example log:

```text
User: Alice

API:
GetObject

Service:
S3
```

Map this event to:

```text
s3:GetObject
```

Another event:

```text
API:
PutObject
```

maps to:

```text
s3:PutObject
```

After analyzing the selected period:

```text
Used Permissions:

s3:GetObject
s3:PutObject
ec2:StartInstances
```

## 10. Compare Permissions

Example:

### Assigned Permissions

```text
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:CreateBucket
ec2:StartInstances
ec2:StopInstances
```

### Used During Last 90 Days

```text
s3:GetObject
s3:PutObject
ec2:StartInstances
```

### Unused Permissions

```text
s3:DeleteObject
s3:CreateBucket
ec2:StopInstances
```

## 11. Recommendation

The system should produce:

### Keep

```text
s3:GetObject
s3:PutObject
ec2:StartInstances
```

### Recommend Removal

```text
s3:DeleteObject
s3:CreateBucket
ec2:StopInstances
```

## 12. Main User Interface

### User Permission Page

Example:

#### User

```text
Alice
AWS / Production
```

#### Analysis

```text
Analysis Period: Last 90 Days

Assigned Permissions: 6
Used Permissions: 3
Unused Permissions: 3
```

#### Permission Table

| Permission         | Assigned Via | Source        | Used | Last Used | Recommendation |
| ------------------ | ------------ | ------------- | ---- | --------- | -------------- |
| s3:GetObject       | Role         | DeveloperRole | Yes  | Aug 17    | Keep           |
| s3:PutObject       | Role         | DeveloperRole | Yes  | Aug 16    | Keep           |
| s3:DeleteObject    | Group        | AdminGroup    | No   | —         | Remove         |
| s3:CreateBucket    | Role         | DeveloperRole | No   | —         | Remove         |
| ec2:StartInstances | Policy       | EC2Developer  | Yes  | Aug 14    | Keep           |
| ec2:StopInstances  | Policy       | EC2Developer  | No   | —         | Remove         |

## 13. System Architecture

```text
                       CIEM

                        │
                        ▼
                 Select User
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼

 Permission Collector            Log Collector

          │                           │
          ▼                           ▼

 User → Group                CloudTrail
      → Role                 GCP Audit Logs
      → Policy               Azure Logs
                             OCI Audit Logs

          │                           │
          ▼                           ▼

 Assigned Permissions          User Activity

          │                           │
          │                           ▼
          │
          │                    Permission Mapper
          │                           │
          │                           ▼
          │                    Used Permissions
          │                           │
          └─────────────┬─────────────┘
                        │
                        ▼
                Comparison Engine
                        │
             ┌──────────┴──────────┐
             ▼                     ▼

          USED                   UNUSED

             │                     │
             ▼                     ▼

           KEEP                  REMOVE
```

## 14. Backend Components

Only three main components are required for the MVP.

### Component 1: Permission Collector

Responsibility:

```text
User
 ↓
Groups / Roles / Policies
 ↓
Permissions
```

Output:

```json
{
  "user": "alice",
  "permission": "s3:GetObject",
  "assigned_via": "ROLE",
  "source": "DeveloperRole"
}
```

### Component 2: Log Analyzer

Responsibility:

```text
User
 ↓
Audit Logs
 ↓
API Operations
 ↓
Permissions Used
```

Output:

```json
{
  "user": "alice",
  "permission": "s3:GetObject",
  "last_used": "2026-08-17",
  "usage_count": 125
}
```

### Component 3: Recommendation Engine

Input:

```text
Assigned Permissions
+
Used Permissions
```

Logic:

```text
IF permission exists in Used Permissions
    → KEEP

IF permission does not exist in Used Permissions
    → REMOVE
```

## 15. Database Model

### Users

```text
users
----------------
id
cloud
account_id
username
```

### User Permission

```text
user_permissions
-------------------------
user_id
permission
assigned_via
source_name
```

Example:

```text
alice | s3:GetObject    | ROLE   | DeveloperRole
alice | s3:PutObject    | ROLE   | DeveloperRole
alice | s3:DeleteObject | GROUP  | AdminGroup
```

### Permission Usage

```text
permission_usage
-------------------------
user_id
permission
first_used
last_used
usage_count
```

Example:

```text
alice | s3:GetObject   | 2026-05-12 | 2026-08-17 | 125
alice | s3:PutObject   | 2026-06-05 | 2026-08-16 | 42
```

## 16. Recommendation Algorithm

Pseudo-code:

```text
assignedPermissions = getPermissions(user)

logs = getLogs(user, lastXDays)

usedPermissions = mapLogsToPermissions(logs)

for permission in assignedPermissions:

    if permission exists in usedPermissions:

        recommendation = KEEP

    else:

        recommendation = REMOVE
```

Equivalent:

```text
KEEP =
Assigned ∩ Used
```

```text
REMOVE =
Assigned - Used
```

## 17. API Design

### Get User Permissions

```text
GET /users/{userId}/permissions
```

Response:

```json
[
  {
    "permission": "s3:GetObject",
    "assignedVia": "ROLE",
    "source": "DeveloperRole"
  }
]
```

### Analyze Permission Usage

```text
POST /users/{userId}/analyze
```

Request:

```json
{
  "days": 90
}
```

Response:

```json
{
  "assigned": 6,
  "used": 3,
  "unused": 3
}
```

### Get Recommendations

```text
GET /users/{userId}/recommendations
```

Response:

```json
[
  {
    "permission": "s3:GetObject",
    "used": true,
    "recommendation": "KEEP"
  },
  {
    "permission": "s3:DeleteObject",
    "used": false,
    "recommendation": "REMOVE"
  }
]
```

## 18. Example End-to-End Flow

User selects:

```text
Alice
AWS Production
Last 90 Days
```

### Step 1

System reads:

```text
Alice
 ↓
DeveloperRole
 ↓
S3DeveloperPolicy
```

and determines:

```text
s3:GetObject
s3:PutObject
s3:DeleteObject
s3:CreateBucket
```

### Step 2

System checks Alice's CloudTrail events from the last 90 days.

Observed:

```text
GetObject
PutObject
```

Mapped to:

```text
s3:GetObject
s3:PutObject
```

### Step 3

Comparison:

```text
Assigned            Used

s3:GetObject         ✓
s3:PutObject         ✓
s3:DeleteObject      ✗
s3:CreateBucket      ✗
```

### Step 4

Recommendation:

```text
KEEP

s3:GetObject
s3:PutObject
```

```text
REMOVE

s3:DeleteObject
s3:CreateBucket
```

## 19. MVP Scope

The MVP needs to answer only three questions:

### 1. What permissions does this user have?

```text
User
→ Group
→ Role
→ Policy
→ Permissions
```

### 2. Which permissions did the user use?

```text
User
→ Audit Logs
→ API Calls
→ Permissions
```

### 3. What permissions should the user keep?

```text
Assigned Permissions
-
Unused Permissions
=
Recommended Permissions
```

No automatic permission changes are required in the MVP.

The system only provides a recommendation.

## 20. Final MVP Definition

{: .important }
> **For a selected cloud user, identify all permissions assigned through groups, roles, policies or direct assignments; analyze cloud audit logs for the last X days to identify permissions actually used; compare assigned permissions with used permissions; and recommend keeping used permissions and removing unused permissions.**

<nav class="doc-pager" aria-label="Document navigation">
  <a class="doc-pager-link is-prev" href="../01-ciem-permission/">
    <span class="doc-pager-label">Previous</span>
    <span class="doc-pager-title">Permission Recommendation</span>
  </a>
  <span></span>
</nav>
