Following listing shows a solution using python to parse the response json and filter only the `access_token` value which is further assigned to an environment variable `token`:

```bash
resource="2ff814a6-3304-4ab8-85cb-cd0e6f879c1d%2F.default"
endpoint=$IDENTITY_ENDPOINT
header="X-Identity-Header: $IDENTITY_HEADER"
apiVersion="2019-08-01"

url="$endpoint?api-version=$apiVersion&resource=$resource"
token=$(curl "$url" -H "$header" | python -c "import json;x=input();y=json.loads(x);print(y['access_token'])")
```

Following approaches could also lead to valid solutions:

* You could do similar with `awk` (well, I am not sure if `awk` supports JSON parsing, but it has regular expressions)
* You could use `sed` and apply regular expression.
* You could use `perl`.
