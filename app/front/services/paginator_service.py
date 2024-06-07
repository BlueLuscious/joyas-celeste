import logging

logger = logging.getLogger(__name__)


class PaginatorService():

    @staticmethod
    def calculate_page_numbers(current_page: int, total_pages: int, max_pages_to_show: int = 5) -> list:

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

        start_page = max(current_page - half_pages_to_show, 1)
        end_page = min(start_page + max_pages_to_show - 1, total_pages)

        if total_pages <= max_pages_to_show:
            start_page = 1
            end_page = total_pages
        elif current_page <= half_pages_to_show:
            end_page = max_pages_to_show
        elif current_page >= total_pages - half_pages_to_show:
            start_page = max(total_pages - max_pages_to_show + 1, 1)

        page_numbers = list(range(start_page, end_page + 1))
        logger.info(f"page numbers: {page_numbers}")
        return page_numbers
