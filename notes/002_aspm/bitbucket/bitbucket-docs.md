---
title: Bitbucket OAuth Setup
parent: ASPM
grand_parent: Notes
nav_order: 5
description: "Registering a Bitbucket Cloud OAuth client, and the token/refresh/clone API calls used to onboard a workspace."
---
{% raw %}

# Bitbucket OAuth Cloud
1. Go to https://bitbucket.org/accuknox-org/workspace/overview/ or,
    Craete a Bitbucket Workspace

2. Go to `Settings` -> `Workspace Settings`

3. Click `Apps and Features` -> `OAuth Clients`

4. Permissions `Read`
    - Account
    - Repositories
    - Pipelines
    - Workspace Membership
    - Pull requests
    - Projects

5. Create `OAuth Client`
    - Client Name  - Accuknox Dev
    - Client ID    - {{client_id}}
    - Client Token - {{client_token}}
    - Redirect Uri - {{redirect_uri}}
    - Auth URL     - {{auth_url}}

6. API to Generate `Access Token`
    - POST https://bitbucket.org/site/oauth2/access_token
    - Auth - Basic - Username (client_id) Password (client_secret)
    - Body - x-www-form-urlencoded
        - grant-type - authorization_code
        - code - from {{Auth URL}}
    - Response
    ```JSON
        {
            "access_token": "ey",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "ey",
            "scope": "pipeline pullrequest project team repository account email",
            "scopes": "pipeline pullrequest project team repository account email"
        }
    ```

7. API to get User Details
    - GET https://api.bitbucket.org/2.0/user
    - Auth - Auth Token

8. API to List Repos
    - GET https://api.bitbucket.org/2.0/repositories/{workspace}
    - Auth - Auth Token

9. API to Refresh `Access Token`
    - POST https://bitbucket.org/site/oauth2/access_token
    - Auth - Basic - Username (client_id) Password (client_secret)
    - Body - x-www-form-urlencoded
        - grant-type - refresh_token
        - refresh_token - from PT.6

10. Clone Repos
    - git clone https://x-token-auth:{{auth_token}}@bitbucket.org/{{workspace}}/{{repo}}.git
{% endraw %}
