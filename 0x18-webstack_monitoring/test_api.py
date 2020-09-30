#!/usr/bin/env python3
from datadog import initialize, api
import json
options = {
    'api_key': '76bf0c453d04f5a1d2dd759ee26ee3eb',
    'app_key': 'ec8bf145d2de4de0581a7e9d4a8bd23b66be19bc'
}

initialize(**options)

print(json.dumps(api.Dashboard.get_all()))
