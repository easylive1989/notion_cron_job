import sys
import json
from repository.notion_api import NotionApi
from repository.habit_repository import HabitRepository, Tdo
from habit_app import HabitApp


if __name__ == '__main__':
	database_dict = json.loads(sys.argv[2])

	notion_api = NotionApi(sys.argv[1])
	notion_repository = HabitRepository(notion_api, database_dict["habit"])
	todo_list_repository = TodoListRepository(notion_api, database_dict["todo_list"])

	habit_app = HabitApp(notion_repository)
	habit_app.add_toady()
