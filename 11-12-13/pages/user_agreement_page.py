from core.base_page import BasePage

class UserAgreementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(lambda d: "user-agreement" in d.current_url)
