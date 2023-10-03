import json, requests, adal


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def queue_build(baseUrl, api, headers, auth, body):
    url = "{}/_apis/build/builds?api-version={}".format(baseUrl, api)

    payload = json.dumps(body)

    response = requests.request('POST', url, headers=headers, data=payload, auth=auth)
    print('Status Code: ', response.status_code)
    print('Response: ', response.text)

def adal_get_access_token():

    # Tenant ID for your Azure Subscription
    TENANT_ID = 'tenant-id'

    # Your Service Principal App ID
    APP_ID = 'client-id'

    # Your Service Principal Password
    SECRET = 'client-secret'

    authority_url = 'https://login.microsoftonline.com/' + TENANT_ID
    context = adal.AuthenticationContext(authority_url)
    token = context.acquire_token_with_client_credentials(
        # resource='https://management.azure.com/',
        # ADO resource ID
        resource='499b84ac-1321-427f-aa17-267ca6975798',
        client_id=APP_ID,
        client_secret=SECRET
    )

    return token
