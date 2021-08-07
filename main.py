import sys
from repository.notion_api import NotionApi
from habit_app import HabitApp


if __name__ == '__main__':

	notion_api = NotionApi(sys.argv[1])

	habit_app = HabitApp(notion_api)
	habit_app.add_toady()
