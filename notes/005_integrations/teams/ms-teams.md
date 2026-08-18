---
title: Microsoft Teams
parent: Integrations
grand_parent: Notes
nav_order: 3
description: "Wiring a Teams workflow webhook to an AccuKnox alert channel, both sides of the integration."
---

# Microsoft Team with AccuKnox

[Here](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet#create-an-incoming-webhook-from-a-template)

## Steps to Integrate with AccuKnox:

### Login into [Teams](https://teams.cloud.microsoft/)
- Go to `Apps`/ `+` Icon
- Select `Workflows` and Category as `All Templates`, Click `Select All`
- Search `Send webhook alerts to a channel` and Select it
- Now, Enter
    - User Friendly `Name` -> Next 
    - Select `Team` and `Channel`
    - Click `Add Workflow`
- Copy the `URL` -> [Example](https://default3c12a671d1f440db858a0329e05ef5.3a.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/a0e212f362cd4bb5b8ef0608d78e0018/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=CVVc-XAYnb0uuDtgkdfi5LNuZ2YzEkz3gtLO9n-Dr-w)

- Now, Go to `Apps`/ `+` Icon -> Workflows
- Click `Manage Workflows`, Select the Created One
- Click `3 Dots`/ `:` then `Edit`
- Remove All Steps apart from 1st One
- Add `New Step`, and Select `Post message in a chat or channel`
- Enter followings:
    - Post As - User
    - Post In - Channel
    - Team
    - Channel
    - Message - `@{string(triggerBody())}`

### Login into AccuKnox
- Go to `Settings` -> `Webhook`
- Enter URL from `Teams`
- Success Code `202`
- Add Header as `content-type: application/json`
- Click `Test` and `Save`