from selenium.webdriver.common.by import By

from base_page import BasePage

class HomePage(BasePage):
    USER_AGREEMENT_LINK = (By.LINK_TEXT, "User Agreement")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.reddit.com/")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_user_agreement(self):
        user_agreement_button = self.wait_for_element(*self.USER_AGREEMENT_LINK)
        user_agreement_button.click()

    GET_APP_BUTTON = (By.ID, "get-app")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.reddit.com/")

    def click_get_app(self):
        get_app_button = self.wait_for_element(*self.GET_APP_BUTTON)
        get_app_button.click()