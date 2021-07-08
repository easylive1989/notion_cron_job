import requests
import json
import sys
from datetime import date

headers = {
	"Content-type": "application/json",
	"Notion-Version": "2021-05-13",
	"Authorization": f"Bearer {sys.argv[1]}"
}

####
#### Add Today
####
print("Add Today...")

today = date.today()
body = {
	"parent": { "database_id": "5e39ba5ba02a40369c99564227a404e5" },
	"properties": {
		"Day": {
			"title": [
				{
					"text": {
						"content": today.strftime("%A"),
					}
				}
			]
		},
		"日期": {
			"date": {
				"start": today.strftime("%Y-%m-%d"),
			}
			
		},
	}
}

result = requests.post(
	"https://api.notion.com/v1/pages", 
	data=json.dumps(body),
	headers=headers
)

print(result.status_code)


