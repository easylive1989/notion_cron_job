from datetime import datetime

class HabitApp:
    def __init__(self, notion_api):
        self.notion_api = notion_api

    def add_toady(self):
        today = datetime.today()
        properties = {
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

        self.notion_api.create_page("5e39ba5ba02a40369c99564227a404e5", properties)