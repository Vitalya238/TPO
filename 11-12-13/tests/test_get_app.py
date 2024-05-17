import pytest
from core.browser_manager import BrowserManager
from core.logger import Logger
from pages.home_page import HomePage

logger = Logger().get_logger()

@pytest.fixture(scope="module")
def setup():
    browser_manager = BrowserManager()
    driver = browser_manager.start_browser()
    yield driver
    browser_manager.quit_browser()

def test_get_app(setup):
    driver = setup
    home_page = HomePage(driver)

    try:
        home_page.click_get_app()
        logger.info("Test Passed.")
    except Exception as e:
        logger.error(f"Test Failed: {e}")
        assert False, f"Test Failed: {e}"
