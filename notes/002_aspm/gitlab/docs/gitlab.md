---
title: GitLab App Setup
parent: ASPM
grand_parent: Notes
nav_order: 7
description: "OAuth setup for GitLab Cloud and personal access tokens for self-hosted GitLab, including token refresh."
---
{% raw %}

# Gitlab Apps (Cloud)
1. Go to `https://gitlab.com/-/user_settings/applications`

2. Click Create New Applications
  2.1 Add Name                (AccuKnox Scan Dev)
  2.2 Redirect Uri            (https://app.dev.accuknox.com/settings)

3. Permission Needed `read_api read_user read_repository`

4. Note the Following
  - AccuKnox Dev Test   - APPLICATION_ID
  - AccuKnox Dev S Test - SECRET
  - Callback URI Test   - https://app.dev-cspm.accuknox.com/settings/integrations?type=gitlabcloud

5. Generate Code (FE should Redirect) - 
  - https://gitlab.com/oauth/authorize?client_id={{APPLICATION_ID}}&redirect_uri={{REDIRECT_URL}}&response_type=code&scope=read_api+read_user+read_repository
    
  - eg: https://gitlab.com/oauth/authorize?client_id=6256ad819442140baec4baf002c6fa312308fcc129b55a19f463cad328520f63&redirect_uri=https://app.dev-cspm.accuknox.com/settings/integrations?type=gitlabcloud&response_type=code&scope=read_api+read_user+read_repository

6. API to get `access` and `refresh` token `https://gitlab.com/oauth/token`

Body - 
{
  "client_id": "{{APPLICATION_ID}}",
  "client_secret": "gloas-",
  "code": "{{CODE FROM FE}}",
  "grant_type": "authorization_code",
  "redirect_uri": "https://oauth.pstmn.io/v1/callback"
}

Response -
{
    "access_token": "{{access_token}}",
    "token_type": "Bearer",
    "expires_in": 7200,
    "refresh_token": "{{refresh_token}}",
    "scope": "read_api read_user read_repository",
    "created_at": 1776337826
}
Valid for 2 Hr (setup cron job to refresh access token from refresh token) (refer pt 8)

7. Clone Repo - git clone https://oauth2:ACCESS_TOKEN@gitlab.com/username/repo.git

git clone https://oauth2:{{access_token}}@gitlab.com/shubham294-group/ak-scan-t.git

8. API to refresh `access` token `https://gitlab.com/oauth/token`

Body - 
{
  "client_id": "{{APPLICATION_ID}}",
  "client_secret": "gloas-",
  "grant_type": "refresh_token",
  "refresh_token": "{{new_refresh_token}}"
}

Response -
{
    "access_token": "{{access_token}}",
    "token_type": "Bearer",
    "expires_in": 7200,
    "refresh_token": "{{refresh_token}}",
    "scope": "read_api read_user read_repository",
    "created_at": 1776353952
}

Note - Refresh Token Also Changed, Need to update Refresh Toke Again in DB

# Gitlab Apps (Self-Hosted)

1. Go to {{BASE_URL}}-/user_settings/personal_access_tokens
  - https://nannie-intercolumnar-starvedly.ngrok-free.dev/-/user_settings/personal_access_tokens

2. Click Create New Token

3. Set Expiry as Needed

4. Permission Needed `read_api read_user read_repository`

5. Save the token - glpat-

6. Store the `base_url` and `token`

7. Clone Repo git clone https://oauth2:{{token}}@gitlab.com/username/repo.git
   - git clone https://oauth2:{{token}}@nannie-intercolumnar-starvedly.ngrok-free.dev/accuknox/accuknox-scan.git

{% endraw %}
