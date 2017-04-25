import requests
import json

header = {"Content-Type": "application/json; charset=utf-8",
          "Authorization": "Basic ZDgwYjk1MmItOGM5Mi00MmFlLWExNjMtZGE0ZWFiZmExNjY2"}

payload = {"app_id": "253ee936-0d98-4b7a-90a7-12c92db25f9d",
           "included_segments": ["Active Users"],
           "contents": {"en": "English Message"}}
 
req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
 
print(req.status_code, req.reason)

#sending notification include rest api key
'''curl --include \
     --request POST \
     --header "Content-Type: application/json; charset=utf-8" \
     --header "Authorization: Basic ZDgwYjk1MmItOGM5Mi00MmFlLWExNjMtZGE0ZWFiZmExNjY2" \
     --data-binary "{\"app_id\": \"253ee936-0d98-4b7a-90a7-12c92db25f9d\",
\"contents\": {\"en\": \"English Message\"},
\"included_segments\": [\"Active Users\"]}" \
     https://onesignal.com/api/v1/notifications'''

#view devices
'''curl --include \
     --header "Authorization: Basic ZDgwYjk1MmItOGM5Mi00MmFlLWExNjMtZGE0ZWFiZmExNjY2" \
     "https://onesignal.com/api/v1/players?app_id={253ee936-0d98-4b7a-90a7-12c92db25f9d}&limit=300&offset=0"'''
