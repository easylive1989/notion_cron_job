from .slack_api import SlackApi
from model.message import Message
from model.exception import MessageNotFoundException

class MessageRepository:
    def get_first_of_message(self, channel: str, text: str, count: int) -> Message:
        pass

class SlackMessageRepository(MessageRepository):
    def __init__(self, slack_api: SlackApi):
        self.slack_api = slack_api


    def get_first_of_message(self, channel: str, text: str, count = 50) -> Message:
        response = self.slack_api.read_channel_history("CHG0JV42J", count)
        messages = map(lambda message: Message.from_dict(message), response["messages"])

        # 找 check point 訊息
        check_point_messages = list(filter(lambda message: text in message.text, messages))
        if len(check_point_messages) <= 0:
            raise MessageNotFoundException(text)

        return check_point_messages[0]