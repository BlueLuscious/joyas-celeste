# import logging
# from django.contrib import messages
# from django_unicorn.components import PollUpdate, UnicornView

# logger = logging.getLogger(__name__)


# class DjangoMessagesView(UnicornView):

#     """ Unicorn Component for Django Messages. """

#     def add_message(self, level: int, message: str) -> None:

#         """ Add message to Django Messages reactively. """

#         logger.info(f"Message: {message} - Level Tag: {level}")
#         if message:
#             messages.add_message(self.request, level, message)
#             logger.info(f"Add message to list: {message}")
#             self.hydrate()
#             return PollUpdate(timing=4000, method=f"remove_message('{message}')")
#         else:
#             logger.info("No new message to add")


#     def remove_message(self, message: str = "") -> PollUpdate:

#         """ Remove message from Django Messages reactively. """

#         if message != "":
#             logger.info(f"Remove message from list: {message}")
#         else:
#             logger.info("No old message to remove")
#         return PollUpdate(disable=True)
        