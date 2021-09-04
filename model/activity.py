from datetime import datetime

class Activity:
    def __init__(self, page_id: str, start_time: str, is_this_week_job: bool):
        self.page_id = page_id
        self.start_time = datetime.strptime(start_time[:10], "%Y-%m-%d")
        self.is_this_week_job = is_this_week_job