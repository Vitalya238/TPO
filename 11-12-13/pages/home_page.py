from selenium.webdriver.common.by import By
from core.base_page import BasePage

class HomePage(BasePage):
    GET_APP_BUTTON = (By.ID, "get-app")
    USER_AGREEMENT_LINK = (By.LINK_TEXT, "User Agreement")
    SEARCH_INPUT = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.reddit.com/")

    def click_get_app(self):
        get_app_button = self.wait_for_element(*self.GET_APP_BUTTON)
        get_app_button.click()

    def click_user_agreement(self):
        user_agreement_button = self.wait_for_element(*self.USER_AGREEMENT_LINK)
        user_agreement_button.click()

    def search(self, query):
        search_input = self.wait_for_element(*self.SEARCH_INPUT)
        search_input.send_keys(query)
        search_input.submit()
