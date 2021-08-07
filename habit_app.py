from datetime import datetime
from repository.habit_repository import HabitRepository

class HabitApp:
    def __init__(self, notion_repository: HabitRepository):
        self.notion_repository = notion_repository

    def add_toady(self):
        today = datetime.today()
        self.notion_repository.add(today.strftime("%A"), today)