from datetime import datetime, timedelta

class TimeProvider:
    def is_yesterday(self, date: datetime) -> bool:
        pass

    def today(self) -> datetime:
        pass
    
    def netxt_first_week_day(self) -> datetime:
        pass

class PyTimeProvider(TimeProvider):
    def is_yesterday(self, date: datetime) -> bool:
        today = date.today()
        yesterday = date.today() - timedelta(days = 1)
        return yesterday.date() == date.date()

    def netxt_first_week_day(self) -> datetime:
        today = datetime.now().today()
        return today - timedelta(days= today.weekday() - 7)

    def today(self) -> datetime:
        return datetime.now().today()