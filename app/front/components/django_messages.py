import logging
from django.contrib import messages
from django.contrib.messages.storage.base import Message
from django.contrib.messages.storage.fallback import FallbackStorage
from django_unicorn.components import PollUpdate, UnicornView

logger = logging.getLogger(__name__)


class DjangoMessagesView(UnicornView):

    """ 
    Unicorn Component for Django Messages. 

    **Bound Properties**:
        **message_list (list[dict])**: List of dictionaries with message data.
    """

    messages_list: list[dict] = []

    def mount(self) -> None:

        """ DjangoMessagesView First Creation. """

        self.update_message_list()


    def get_messages(self) -> list[Message]:
        storage: FallbackStorage = messages.get_messages(self.request)
        storage.used = True
        logger.info(f"Get Django Messages: {list(storage)}")
        return list(storage)


    def add_message(self, level: int = 0, text: str = "") -> PollUpdate | None:

        """ Add the first message from Django Messages to `message_list` reactively. """


        if level and text != "":
            messages.add_message(self.request, level, text)

        storage = self.get_messages()
        message = next(iter(storage), None)

        if message:
            new_message = dict(text=message.message, level_tag=message.level_tag)
            self.messages_list.append(new_message)
            self.update_message_list(self.messages_list)
            logger.info(f"Add message to list: {new_message.get('text')}")
            
            if len(self.messages_list) == 1:
                return PollUpdate(timing=3000, method="remove_message")
        else:
            logger.info("No new message to add")
            self.update_message_list(self.messages_list)
            return PollUpdate(disable=True)


    def remove_message(self) -> PollUpdate:

        """ Remove the first message from `message_list` reactively. """

        if self.messages_list:
            message: dict = self.messages_list.pop(0)
            logger.info(f"Remove message from list: {message.get('text')}")
            self.update_message_list(self.messages_list)

            if len(self.messages_list) > 0:
                return PollUpdate(timing=3000, method="remove_message")
        return PollUpdate(disable=True)
            

    def clear_message_list(self) -> None:

        """ Clear entire `message_list` reactively. """

        self.messages_list.clear()
        

    def update_message_list(self, message_list: list = []) -> None:

        """ Update `message_list` reactively. """

        self.messages_list = message_list
