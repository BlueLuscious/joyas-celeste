import logging
from django.core.paginator import Page, Paginator

logger = logging.getLogger(__name__)


class PageService:

    """ Service for Page """

    def __init__(self, page: Page) -> None:

        """ 
        PageService Initializer.

        Args:
            page (Page): A Page Instance.
        """

        self.page = page


    def page_data_as_dict(self, pagination: Paginator) -> dict:

        """
        Get page data as dictionary.

        Args:
            pagination (Paginator): A Paginator Instance.

        Returns:
            dict: A dictionary with Page data.
        """

        page_data = dict(
            has_other_pages=self.page.has_other_pages(),
            has_previous=self.page.has_previous(),
            has_next=self.page.has_next(),
            previous_page_number=self.page.previous_page_number() if self.page.number > 1 else None,
            next_page_number=self.page.next_page_number() if self.page.number != pagination.num_pages else None,
            number=self.page.number,
        )
        logger.info(f"Page data: {page_data}")
        return page_data
    

    def get_pagination_controls_range(self, total_pages: int, max_pages_to_show: int = 5) -> list:

        """
        Calculate the list of page numbers to display in pagination.

        Args:
            current_page (int): The current page number.
            total_pages (int): The total number of pages.
            max_pages_to_show (int): The maximum number of pages to show.

        Returns:
            list: A list of page numbers to display in pagination.
        """

        half_pages_to_show = max_pages_to_show // 2

        start_page = max(self.page.number - half_pages_to_show, 1)
        end_page = min(start_page + max_pages_to_show - 1, total_pages)

        if total_pages <= max_pages_to_show:
            start_page = 1
            end_page = total_pages
        elif self.page.number <= half_pages_to_show:
            end_page = max_pages_to_show
        elif self.page.number >= total_pages - half_pages_to_show:
            start_page = max(total_pages - max_pages_to_show + 1, 1)

        page_numbers = list(range(start_page, end_page + 1))
        logger.info(f"Pagination controls range: {page_numbers}")
        return page_numbers
    