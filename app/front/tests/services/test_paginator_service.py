from django.test import TestCase
from front.services.paginator_service import PaginatorService


class PaginatorServiceTest(TestCase):
    def setUp(self):
        pass


    def test_calculate_page_numbers(self):
        default_current_page = 1
        default_total_pages = 5
        default_max_pages_to_show = 5
    
        list_page_numbers = PaginatorService.calculate_page_numbers(default_current_page, default_total_pages, default_max_pages_to_show)
        self.assertLessEqual(len(list_page_numbers), default_max_pages_to_show)
