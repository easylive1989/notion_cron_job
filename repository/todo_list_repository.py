from .notion_api import NotionApi

class TodoListRepository:
    def __init__(self, notion_api: NotionApi, database_id: str):
        self.notion_api = notion_api
        self.database_id = database_id

    def get_activities(self):
        filter_body = {
            "filter": {
                "property": "清單",
                "select": {
                    "equals": "會議活動"
                }
            }
        }

        self.notion_api.query_database(self.database_id, filter_body)