from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage

class Application:

    def __int__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)