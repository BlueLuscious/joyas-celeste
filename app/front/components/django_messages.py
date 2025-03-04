import logging
from django.contrib import messages
from django.contrib.messages.storage.base import Message
from django.contrib.messages.storage.fallback import FallbackStorage
from django.utils.timezone import now, datetime
from django_unicorn.components import PollUpdate, UnicornView
from app.utils.message_o import MessageO

logger = logging.getLogger(__name__)


class DjangoMessagesView(UnicornView):

    """ 
    Unicorn Component for Django Messages. 

    **Bound Properties**:
        **message_list (list[dict])**: List of dictionaries with message data.
    """
    
    messages_list: list[dict] = []
    is_poll_disable: bool = True

    def mount(self):

        """ DjangoMessagesView First Creation. """

        self.messages_list = []
        storage: FallbackStorage = messages.get_messages(self.request)
        storage.used = True
        self.storage = list(storage)


    def add_django_message(self) -> PollUpdate | None:

        """ Add message from Django Messages to `message_list` reactively. """

        if self.storage:
            logger.info(f"Get Django Messages: {self.storage}")
            message: Message = next(iter(self.storage), None)
            self.messages_list.append(MessageO(message.message, message.level).to_dict())
            logger.info(f"Add message to list: {message.message}")

            if self.is_poll_disable:
                self.is_poll_disable = False
                return PollUpdate(timing=3000, method="clean_messages")
        else:
            logger.info("No new django message to add")


    def add_message(self, level: int = 0, text: str = "") -> PollUpdate | None:

        """
        Add message to `message_list` reactively.

        Args:
            level (int): Message level.
            text (str): Message text.
        """

        if level and text != "":
            self.messages_list.append(MessageO(text, level).to_dict())
            logger.info(f"Add message to list: {text}")

            if self.is_poll_disable:
                self.is_poll_disable = False
                return PollUpdate(timing=3000, method="clean_messages")
        else:
            logger.info("No new message to add")


    def clean_messages(self) -> PollUpdate | None:

        """ Remove expired messages from `message_list` reactively. """

        if self.messages_list:
            logger.info(f"Current messages in list: {self.messages_list}")
            self.messages_list = [m for m in self.messages_list if now() < datetime.fromisoformat(m["expire_at"])]
            logger.info(f"Oldest messages in list: {self.messages_list}")

            if not self.messages_list and not self.is_poll_disable:
                self.is_poll_disable = True
                return PollUpdate(disable=True)
        else:
            logger.info(f"No old messages in list to clean")
        