import sys
import json
from repository.notion_api import NotionApi
from repository.habit_repository import HabitRepository
from repository.todo_list_repository import TodoListRepository
from service.time_provider import PyTimeProvider
from habit_app import HabitApp
from todo_list_app import TodoListApp


if __name__ == '__main__':
	database_dict = json.loads(sys.argv[2])

	notion_api = NotionApi(sys.argv[1])
	time_provider = PyTimeProvider()
	notion_repository = HabitRepository(notion_api, database_dict["habit"])
	todo_list_repository = TodoListRepository(notion_api, database_dict["todo_list"])

	habit_app = HabitApp(notion_repository)
	habit_app.add_toady()

	todo_list_app = TodoListApp(todo_list_repository, time_provider)
	todo_list_app.move_this_week_activities()
