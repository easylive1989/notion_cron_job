from .notion_api import NotionApi
from model.activity import Activity
from datetime import datetime

class TodoListRepository:
    def __init__(self, notion_api: NotionApi, database_id: str):
        self.notion_api = notion_api
        self.database_id = database_id

    def get_activities(self, after: datetime) -> list:
        filter_body = {
            "filter": {
                "and": [
                    {
                        "property": "清單",
                        "select": {
                            "equals": "會議活動"
                        }
                    },
                    {
                        "property": "Deadline",
                        "date": {
                            "after": after.strftime("%Y-%m-%d")
                        }
                    },
                ],
            }
        }

        response = self.notion_api.query_database(self.database_id, filter_body)
        return map(lambda result: Activity(result["id"], result["properties"]["Deadline"]["date"]["start"], result["properties"]["本週任務"]["checkbox"]), response.json()["results"])

    def move_activities_to_this_week(self, page_id: str):
        body = {
  		    "properties": {
        		"本週任務": { 
            		"checkbox": True
        		}
  	    	}
	    }

        self.notion_api.patch_page(page_id, body)