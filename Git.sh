ServicePrincipalAadAccessToken={access-token}
git -c http.extraheader="AUTHORIZATION: bearer $ServicePrincipalAadAccessToken" clone {git-uri}
git -c http.extraheader="AUTHORIZATION: bearer $ServicePrincipalAadAccessToken" push origin master