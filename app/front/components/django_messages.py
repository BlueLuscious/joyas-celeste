from django.contrib.messages import get_messages
from django.contrib.messages.storage.base import Message
from django.contrib.messages.storage.fallback import FallbackStorage
from django_unicorn.components import UnicornView


class DjangoMessagesView(UnicornView):
    messages_list: list = []

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def add_message(self) -> None:
        storage: FallbackStorage = get_messages(self.request)
        for message in storage:
            message: Message
            msg: dict = {
                "text": message.message,
                "level_tag": message.level_tag
            }
            self.messages_list.append(msg)


    def remove_message(self) -> None:
        if self.messages_list:
            self.messages_list.pop(0)
            

    def clean_message_list(self) -> None:
        self.messages_list.clear()
        