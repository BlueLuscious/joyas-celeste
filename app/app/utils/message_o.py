from django.contrib import messages
from django.utils.timezone import now, timedelta


class MessageO:

    """
    Message Entity. 
    
    Fields:
        text (str): Message text.
        level (int): Message level.
        level_tag (int): Message level tag.
        expire_time (int): Message expiration date.
    """
    
    def __init__(self, text: str, level: int, expire_time: int = 3000) -> None:

        """ Message Initializer. """

        self.text = text
        self.level = level
        self.level_tag = self.get_level_tag(level)
        self.expire_at = now() + timedelta(milliseconds=expire_time)
    

    def to_dict(self) -> dict:

        """ Returns a dict of the Message data. """

        return dict(
            text=self.text,
            level=self.level,
            level_tag=self.level_tag,
            expire_at=self.expire_at.isoformat()
        )
    

    def get_level_tag(self, level: int) -> str:
        if level == messages.SUCCESS:
            tag = "success"
        elif level == messages.WARNING:
            tag = "warning"
        elif level == messages.ERROR:
            tag = "error"
        elif level == messages.INFO:
            tag = "info"
        elif level == messages.DEBUG:
            tag = "debug"
        else:
            tag = ""
        return tag
    