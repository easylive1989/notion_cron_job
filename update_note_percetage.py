import requests
import json
import sys

headers = {
	"Content-type": "application/json",
	"Notion-Version": "2021-05-13",
	"Authorization": f"Bearer {sys.argv[1]}"
}

####
#### Read Areas
####
print("Read Database...")

query_body = {
	"filter": {
  		"property": "分類",
  		"select": {
    		"equals": "專業"
  		}
	}
}
response = requests.post(
	"https://api.notion.com/v1/databases/bf60f206f1214aefa24fb16b48a5b791/query",
	data=json.dumps(query_body),
	headers=headers
)

body = response.json()["results"]
# print(body)

####
#### Calculate Total Notes
####
print("Calculating...")


update_list = []

for page in body:
	update_list.append({
		"id": page["id"],
		"note_count": len(page["properties"]["筆記與靈感"]["relation"])
	})

#print(update_list)

####
#### Update Percetage For Each Row
####
print("Updating...")


total_notes_count = sum(data["note_count"] for data in update_list)
for data in update_list:
	notes_percetage = round(data["note_count"] / total_notes_count, 4)
	body = {
  		"properties": {
    		"等級百分比": { 
        		"number": notes_percetage,
        		"format" : "percent"
    		}
  		}
	}

	result = requests.patch(
		"https://api.notion.com/v1/pages/" + data["id"], 
		data=json.dumps(body),
		headers=headers
	)

	#print(f"status: {result.status_code} percetage: {notes_percetage}")
