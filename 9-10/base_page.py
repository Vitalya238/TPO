from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
