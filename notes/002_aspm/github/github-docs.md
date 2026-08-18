---
title: GitHub App Setup
parent: ASPM
grand_parent: Notes
nav_order: 6
description: "Registering a GitHub App, its permissions, and the JWT → installation token flow used to clone repos."
---

# Github Apps 
Refer (https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)
1. Go to `https://github.com/settings/apps`

2. Click Create `New Github App`
  2.1 Github App Name                                     (ASPM)
  2.2 Home Page URL                                       (https://app.dev.accuknox.com/)
  2.3 Callback URL                                        (https://app.dev.accuknox.com/settings) (ignore)
  2.4 Expire user authorization tokens                    (Enabled)
  2.5 Post installation -> Setup URL   (Mandatory)        (https://app.dev.accuknox.com/settings)
  2.6 Redirect on Update                                  (Disabled)
  2.7 Webhook (used for getting alerts)                   (Wehook URL and Secret)

3. Permission Needed (Read-Only)
    - **Repository** 
      - Administration 
      - Checks
      - Contents
      - Metadata
      - Pull requests
      - Deployments
      - Commit Statuses

    - **Organisation**
      - Administration
      - Members


    - **Account Permission**
      - Email addresses


    - **Events**
      - Pull request
      - Repository
      - Push

4. Note the Following
  - App Id - {{APP-ID}}
  - Client Id - {{Client-ID}}
  - Download Private Key

5. Install App - https://github.com/apps/{{APP_NAME}}/installations/new

6. When App Installed Note- Installation ID (Very Imp)

7. Create JWT (jwt.io) (max time 10 mins)
  7.1 Algorithm & Token Type
      {
        "alg": "RS256",
        "typ": "JWT"
      }
  
  7.2 Payload 
      {
        "iat": start-time,
        "exp": end-time,
        "iss": "appilication-id"
      }
  
  7.3 Sign JWT (Github Pem File)

  Save JWT

8. Get Github Token
  8.1 @get-access-token -> Save the Output -> TimeZone (UTC) (Valid for 1 Hr)
  8.2 Need to Re-generate based on expiry

9. Clone Repo - 
  - git clone https://x-access-token:{{ACCESS-TOKEN}}@github.com/{{ORG}}/{{REPO}}.git

  - https://x-access-token:ghs_ABCXYZ@github.com/USERNAME/REPO1.git
