import logging
from django.contrib.messages import get_messages
from django.contrib.messages.storage.base import Message
from django.contrib.messages.storage.fallback import FallbackStorage
from django_unicorn.components import UnicornView

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


    def add_message(self) -> None:

        """ Add the first message from Django Messages to `message_list` reactively. """

        storage: FallbackStorage = get_messages(self.request)
        message: Message = None

        if len(list(storage)) >= 1:
            message = list(storage)[0]

        if message:
            new_message = dict(text=message.message, level_tag=message.level_tag)
            self.messages_list.append(new_message)
            self.update_message_list(self.messages_list)
            self.call("hideMessages")
            logger.info(f"Add message to list: {new_message.get('text')}")
        else:
            logger.info("No new message to add")


    def remove_message(self) -> None:

        """ Remove the first message from `message_list` reactively. """

        if self.messages_list:
            message: dict = self.messages_list.pop(0)
            logger.info(f"Remove message from list: {message.get('text')}")
        self.update_message_list(self.messages_list)
            

    def clear_message_list(self) -> None:

        """ Clear entire `message_list` reactively. """

        self.messages_list.clear()
        

    def update_message_list(self, message_list: list = []) -> None:

        """ Update `message_list` reactively. """

        self.messages_list = message_list
