---
title: Jira
parent: Integrations
grand_parent: Notes
nav_order: 1
description: "APIs to fetch Jira Epics and Stories, and how ticket type maps to task vs. sub-task creation."
---

# Jira

API to fetch all EPIC's and Stories

API 1 -> https://{{base_url}}/rest/api/3/search/jql?jql=project= {{project_key}} AND issuetype in (Story,Epic)&fields=summary,issuetype
API 2 -> https://{{base_url}}/rest/api/3/search/jql?jql=project= {{project_key}} AND issuetype in (Story,Epic) AND summary  ~ "{{search_text}}" &fields=summary,issuetype

Response
```JSON
{
    "issues": [
        {
            "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",
            "id": "2874204",
            "self": "https://accu-knox.atlassian.net/rest/api/3/issue/2874204",
            "key": "QJ-20492",
            "fields": {
                "summary": "Story Under Epic",
                "issuetype": {
                    "self": "https://accu-knox.atlassian.net/rest/api/3/issuetype/10147",
                    "id": "10147",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://accu-knox.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": false,
                    "avatarId": 10315,
                    "entityId": "ae9bbb31-9473-437a-ab93-fb5c687d43d8",
                    "hierarchyLevel": 0
                }
            }
        },
        {
            "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",
            "id": "2874188",
            "self": "https://accu-knox.atlassian.net/rest/api/3/issue/2874188",
            "key": "QJ-20490",
            "fields": {
                "summary": "EPIC 1",
                "issuetype": {
                    "self": "https://accu-knox.atlassian.net/rest/api/3/issuetype/10148",
                    "id": "10148",
                    "description": "Epics track collections of related bugs, stories, and tasks.",
                    "iconUrl": "https://accu-knox.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10307?size=medium",
                    "name": "Epic",
                    "subtask": false,
                    "avatarId": 10307,
                    "entityId": "ce625155-5f6e-478a-aabf-afa8c6bd8be6",
                    "hierarchyLevel": 1
                }
            }
        }
    ],
    "nextPageToken": "ChkjU3RyaW5nJlVVbz0lSW50Jk1UZzNPVGc9EDIYmMXfiuIzIihwcm9qZWN0PVFKIEFORCBpc3N1ZXR5cGUgaW4gKFN0b3J5LEVwaWMpKgJbXQ==",
    "isLast": false
}```

Things to Consider
1. key -> Ticket Id
2. fields.summary -> Title
3. fields.issuetype.name -> Type (Epic/Story)
4. If fields.issuetype.name == Epic create Task under Epic
   elif fields.issuetype.name ==Story create Sub-Task Under Story
5. API is Paginated

