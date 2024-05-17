from base_page import BasePage


class UserAgreementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_url_contains("user-agreement")
