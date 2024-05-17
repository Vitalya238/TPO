from selenium.webdriver.common.by import By
from core.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".search-result")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(*self.SEARCH_RESULTS)

    def get_search_results(self):
        return self.driver.find_elements(*self.SEARCH_RESULTS)
