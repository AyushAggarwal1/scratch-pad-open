---
title: Event Trail
parent: Notes
nav_order: 6
description: "PRD: a unified action/alert log for the CNAPP platform — RabbitMQ → MongoDB pipeline, generic log schema, and per-component payload examples."
---

# \[PRD\]: Event\-Trail Logs and Alerts

| **Target release** | Type // to add a target release date |
| --- | --- |
| **Epic** | Type /Jira to add Jira epics and issues |
| **Document status** | DEVELOPMENT IN PROGRESS |
| **Document owner** | @Ayush Aggarwal@Rahul Jadhav |
| **CSPM Dev** | @Vighnesh Vasu Vats |
| **Designer** | @balaji@Dinesh Kumar S |
| **Tech lead** | @ lead |
| **Technical writers** | @ writers |
| **QA** |  |
| **Linked Documents** | 1. <https://accu-knox.atlassian.net/wiki/x/BQD3QQ>  2. <https://accu-knox.atlassian.net/wiki/x/FQAcN> |

## **🧠 Problem Statement**

Our CNAPP platform has many features (like Rule Engine, User Management, etc.), but we don’t track their internal actions.

Examples:

- Rule Engine fails to create a ticket → no visibility.
- User invited another user → we don’t know who invited whom or with what role.
- Finding status changed by a Specific user → no record.

This creates blind spots for users and internal teams.

We need a way to **track** and **store** all these actions in one place.

##  Objective

Create a system that keeps a record of actions and alerts in our platform, so we can see:

- What happened
- Who did it
- When it happened
- Whether it worked or failed
- Track all internal actions
- Store logs in a structured way
- Allow users to view and filter them
- Notify (optional) when certain actions fail

### **🏗️ \[BE\] Architecture Overview**

Here’s how the data will travel:

1. Microservice sends a message to RabbitMQ (a message bus)
2. Another service takes that message and stores it in MongoDB
3. Our SaaS UI will call APIs to show this log to users

## 📦 Schema for Logs

### ✅ Generic Log Schema (Applies to all actions)

```
{
  "id": "uuid",                      // Unique log ID
  "timestamp": "date-time",          // When it happened
  "tenant_id": "19",
  "component": "Rule Engine",  | "Vulnerability Management" | "User Management"       // Source microservice/component
  "type": "action" | "alert",
  "action": "create_ticket" | "send_to_notification" | "change_status",  // Specific action name
  "user": "ayush@accuknox.com" | "system",
  "result": "ok" | "fail" | "warn",
  "message": "Rule executed successfully",
  "payload": { ... }                 // Detailed info
}
```


### **🔍 Examples of Payloads (Based on Use Case)**

1. Rule Engine – Ticket Created
    1. For Summary Result

```
{
  "rule_id": "rule-123",
  "triggered_on": "date-time",
  "confriguation_name": "conf-for-RE",
  "integration_name": "jira" | "freshservice" | "manage-engine",
  "status": "created n number of tickets"
  "summary": {
    "total_tickets": 18,
    "successful": 15,
    "sucessful_tickets_id": "uuid1, uuid2........."
    "failed": 3
  }
}
```
    2. For Individual Ticket

```
{  
  "ticket_id": NULL
  "finding_id": "finding-def",
  "error": "Jira API rate-limited the request",
}
```
2. Rule Engine - Send to Notification

```
{
  "rule_id": "rule-27",
  "triggered_on": "date-time",
  "integration_name": "Slack",
  "channel_id": "slack-001",
  "status": "sned n number of notification",
  "summary":" {
    "total": 18,
    "successful": 15,
    "failed": 3
  }
}
```
3. User Invited

```
{
  "invited_user": "ravi@accuknox.com",
  "role_assigned": "Viewer" | "Admin" | "Editor", 
  "invite_status": "sent" | "accepted"
}
```
4. Finding Status changed by User

```
{
  "finding_id": "uuid",
  "finding_name": "detect secret",
  "date_type": "cmx-sca",
  "previous_status": "Active",
  "new_status": "Accepted Risk"
}
```

##  Requirements

| **User Persona** | **User Story** | **Use Case** |
| --- | --- | --- |
| Platform Administrator | As a platform admin, I want to: - View all actions the system or users take so I can audit activity. - Know when a rule fails or behaves unexpectedly, so I can debug faster. - See who invited which user and what role they got, for access transparency. | - Who gave editor access to <ayush@accuknox.com>? - Did any failed user invites occur last week? - Audit user activity during a security incident |
| Security Engineer  | As a security engineer, I want to: - Track changes made by automation (e.g., finding status updated), so I can verify the logic. - Filter logs by component or time range, to investigate incidents easily. - Be notified if any critical action (e.g., ticket creation or remediation) fails, so I can act immediately. | - Why did Rule-17 not trigger a Jira ticket? - Was the finding status changed by a user or the system? |
| Viewer | Search structured logs during | - Review logs - Show all system actions taken between April 1–15 - Confirm the timing of finding closure for an incident report |

## ⿻ Wireframes

1. The user clicks on **Monitors / Alerts** and then selects **Alerts**.


1. From the dropdown menu, the user chooses **AccuKnox Audit Service**.


1. Main Table View

```
| Timestamp | Component   |     Action    | Result |          User      |             Message              | 
|-----------|-------------|---------------|--------|--------------------|----------------------------------|
| 12:01 PM  | Rule Engine | create_ticket | PASS   | system             | Created Jira ticket JIRA-1001    |
| 12:03 PM  | Rule Engine | create_ticket | FAIL   | system             | Failed to create ticket: timeout |
| 12:10 PM  | User Mgmt   | invite_user   | FAIL   | ayush@accuknox.com | Invited to ravi@accuknox.com     |
```

1. Detail View (Raw Logs)

Sample Logs

1. Findings 

```
{
  "id": "d19e77e3-4477-4a92-b850-0384da7eff42",
  "timestamp": "2025-07-22 05:34:53.195310+00:00",
  "tenant_id": "5",
  "component": "Vulnerability Management",
  "type": "action",
  "action": "findings-status-updated",
  "user": "vighneshvats@accuknox.com",
  "result": "Ok",
  "message": "Findings Status Updated",
  "payload": [
    {
      "id": "00033f1f-8f30-45aa-a215-85fb30952f5d",
      "name": "linux-libc-dev: 6.1.129-1 : CVE-2024-57950",
      "data_type": "cx_containers",
      "previous_status": "Fixed",
      "new_status": "Active"
    }
  ]
}
```
2. User Invited 
    1. Sucess 

```
{
  "id": "51b0cde9-fa21-478e-a696-0c03f09faf29",
  "timestamp": "2025-06-27 04:54:29.333526+00:00",
  "tenant_id": "5",
  "component": "User Management",
  "type": "action",
  "action": "user_invited",
  "user": "vighneshvats@accuknox.com",
  "result": "Ok",
  "message": "User Invited",
  "payload": {
    "invited_user": "user12@example.com",
    "role_assigned": "Admin",
    "invite_status": "sent"
  }
}
```
    2. Failed 

```
{
  "id": "4162afee-2a89-4650-b830-16a5c0478fa5",
  "timestamp": "2025-06-30 03:54:31.481586+00:00",
  "tenant_id": "5",
  "component": "User Management",
  "type": "action",
  "action": "user_invited",
  "user": "vighneshvats@accuknox.com",
  "result": "Fail",
  "message": "User profile with email user12@example.com already exists.",
  "payload": {}
}
```
3. Ticket

## **🔜 Future Enhancements**

- Grouping by user or action
-  Role-based Access Control for Logs
- …….

## 🔧 Filters & Search

Users should be able to filter logs by:

- Component
- Action Type
- Result (ok, fail, warn)
- User
- Date Range

## Real Logs



##  User interaction and design

Type /image to add mockups, diagrams, and screenshots related to the requirements.


##  Open Questions

| **Question** | **Answer** | **Date Answered** |
| --- | --- | --- |
| e.g., How might we make users more aware of this feature? | e.g., We'll announce the feature with a blog post and a presentation | Type // to add a date |

##  Out of Scope

List the features discussed which are out of scope or might be revisited in a later release.

-
