from django.contrib import messages
from django_unicorn.components import UnicornView


class DjangoMessagesView(UnicornView):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def display_messages(self, message: str, level: str) -> None:
        if level == "success":
            messages.success(self.request, message)
        if level == "error":
            messages.error(self.request, message)
            