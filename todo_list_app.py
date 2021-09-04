from repository.todo_list_repository import TodoListRepository
from service.time_provider import TimeProvider

class TodoListApp:
    def __init__(self, todo_list_repository: TodoListRepository, time_provider: TimeProvider):
        self.todo_list_repository = todo_list_repository
        self.time_provider = time_provider

    def move_this_week_activities(self):
        activities = self.todo_list_repository.get_activities(self.time_provider.today())
        for activity in activities:
            if activity.start_time < self.time_provider.netxt_first_week_day():
                self.todo_list_repository.move_activities_to_this_week(activity.page_id)