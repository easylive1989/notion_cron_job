from datetime import datetime
from .notion_api import NotionApi

class HabitRepository:
    def __init__(self, notion_api: NotionApi, database_id: str):
        self.notion_api = notion_api
        self.database_id = database_id

    def add(self, title: str, start: datetime):
        properties = {
            "Day": {
                "title": [
                    {
                        "text": {
                            "content": title,
                        }
                    }
                ]
            },
            "日期": {
                "date": {
                    "start": start.strftime("%Y-%m-%d"),
                }
                
            },
        }

        self.notion_api.create_page(self.database_id, properties)