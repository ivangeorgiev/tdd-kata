# Problem

For Azure AppService I want to acquire bearer token for Azure Databricks, using managed identity. For this purpose, I am running following command:

```bash
resource="2ff814a6-3304-4ab8-85cb-cd0e6f879c1d%2F.default"
endpoint=$IDENTITY_ENDPOINT
header="X-Identity-Header: $IDENTITY_HEADER"
apiVersion="2019-08-01"

$ curl "$url" -H "$header"
```
The output is a JSON:

```json
{"access_token":"<some-very-long-string>","expires_on":"1709046738","resource":"2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default","token_type":"Bearer","client_id":"abcd"}
```

For my next command I need only the `access_token` value from the response JSON.

I am not allowed to install anything so cannot use `jq`.

