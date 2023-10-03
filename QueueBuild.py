#!/usr/bin/python
# -*- coding: UTF-8 -*-

from requests.auth import AuthBase
from tool import BearerAuth, queue_build, adal_get_access_token


Organization = 'your-organization'
Project = 'your-project-name'
ApiVersion = '7.0'

# Get Access Token
access_token_obj = adal_get_access_token()
access_token = access_token_obj['accessToken']
expire_date = access_token_obj['expiresOn']

print('::: Get Access Token Successfully!')
print('Expire Date: ', expire_date)
print('Your token here (remove this line when prod): ', access_token)


# Queue Build
base_url = 'https://dev.azure.com/{}/{}'.format(Organization, Project)
headers = {
  'Content-Type': 'application/json'
}

auth = BearerAuth(access_token)
body = {
  'definition': {
    'id': 29 # replace with your build definition id in target project
  }
}
print('Queue Build ...')
queue_build(base_url, ApiVersion, headers, auth, body)