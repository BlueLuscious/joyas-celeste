from django.core.paginator import Page, Paginator
from front.utils.context import Context

class PageService:

    def __init__(self, page: Page,) -> None:
        self.page = page

    def page_data_as_dict(self, pagination: Paginator) -> dict:
        page_data = Context(
            has_other_pages=self.page.has_other_pages(),
            has_previous=self.page.has_previous(),
            has_next=self.page.has_next(),
            previous_page_number=self.page.previous_page_number() if self.page.number > 1 else None,
            next_page_number=self.page.next_page_number() if self.page.number != pagination.num_pages else None,
            number=self.page.number,
        )
        return page_data.as_dict
    