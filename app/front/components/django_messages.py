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

    def __init__(self, *args, **kwargs) -> None:

        """ DjangoMessagesView Initializer. """

        super().__init__(*args, **kwargs)


    def add_message(self) -> None:

        """ 
        Add the last message from Django Messages to a list reactively.

        Add a dict with message data in `message_list`:
            **text (str)**: Message.
            **level_tag (str)**: Message Level.
        """

        storage: FallbackStorage = get_messages(self.request)
        message: Message = None

        for message_in_storage in storage:
            message = message_in_storage

        if message:
            new_message: dict = {
                "text": message.message,
                "level_tag": message.level_tag
            }
            self.messages_list.append(new_message)
            self.call("hideMessages")
            logger.info(f"Add message to list: {new_message.get('text')}")
        else:
            logger.info("No new message to add")


    def remove_message(self) -> None:

        """ Remove the first message from `message_list` reactively. """

        if self.messages_list:
            message: dict = self.messages_list.pop(0)
            logger.info(f"Remove message from list: {message.get('text')}")
            

    def clear_message_list(self) -> None:

        """ Clear entire `message_list` reactively. """

        self.messages_list.clear()
        