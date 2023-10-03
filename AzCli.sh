az login --service-principal -u {client-id} -p {client-secret} --tenant {tenant-id}
az account get-access-token --resource 499b84ac-1321-427f-aa17-267ca6975798 --query "accessToken" --output tsv