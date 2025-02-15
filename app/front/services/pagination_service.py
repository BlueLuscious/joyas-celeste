import logging
from typing import Any
from django.core.paginator import Paginator
from django.db.models import QuerySet

logger = logging.getLogger(__name__)


class PaginatorService:

    """ Service for Paginator """

    def __init__(self, pagination: Paginator, page_number: int = 1) -> None:

        """ 
        PaginatorService Initializer.

        Args:
            pagination (Paginator): A Paginator Instance.
            page_number (int): Number to get a Page Instance.
        """

        self.pagination = pagination
        self.page = self.pagination.get_page(page_number)


    def page_data_as_dict(self) -> dict:

        """
        Get page data as dictionary.

        Returns:
            dict: A dictionary with Page data.
        """

        page_data = dict(
            has_other_pages=self.page.has_other_pages(),
            has_previous=self.page.has_previous(),
            has_next=self.page.has_next(),
            previous_page_number=self.page.previous_page_number() if self.page.number > 1 else None,
            next_page_number=self.page.next_page_number() if self.page.number != self.pagination.num_pages else None,
            number=self.page.number,
        )
        logger.info(f"Page data: {page_data}")
        return page_data
    

    def get_object_list(self) -> QuerySet[Any]:

        """
        Get paginated objects from a Page.
        
        Returns:
            QuerySet[Any]: QuerySet of a Model.
        """

        return self.page.object_list
    

    def get_pagination_controls_range(self, max_pages_to_show: int = 5) -> list:

        """
        Calculate the list of page numbers to display in pagination.

        Args:
            max_pages_to_show (int): The maximum number of pages to show.

        Returns:
            list: A list of page numbers to display in pagination.
        """

        half_pages_to_show = max_pages_to_show // 2

        start_page = max(self.page.number - half_pages_to_show, 1)
        end_page = min(start_page + max_pages_to_show - 1, self.pagination.num_pages)

        if self.pagination.num_pages <= max_pages_to_show:
            start_page = 1
            end_page = self.pagination.num_pages
        elif self.page.number <= half_pages_to_show:
            end_page = max_pages_to_show
        elif self.page.number >= self.pagination.num_pages - half_pages_to_show:
            start_page = max(self.pagination.num_pages - max_pages_to_show + 1, 1)

        page_numbers = list(range(start_page, end_page + 1))
        logger.info(f"Pagination controls range: {page_numbers}")
        return page_numbers
    