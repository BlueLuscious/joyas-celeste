from django_unicorn.components import UnicornView


class DjangoMessagesView(UnicornView):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def display_messages(self) -> None:
        pass