import pytest
from core.browser_manager import BrowserManager
from core.logger import Logger
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

logger = Logger().get_logger()

@pytest.fixture(scope="module")
def setup():
    browser_manager = BrowserManager()
    driver = browser_manager.start_browser()
    yield driver
    browser_manager.quit_browser()

def test_search(setup):
    driver = setup
    home_page = HomePage(driver)

    try:
        home_page.search("selenium testing")
        search_results_page = SearchResultsPage(driver)
        results = search_results_page.get_search_results()

        assert results, "No search results found"
        logger.info("Search Test Passed.")
    except Exception as e:
        logger.error(f"Test Failed: {e}")
        assert False, f"Test Failed: {e}"
