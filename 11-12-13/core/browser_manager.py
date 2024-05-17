from selenium import webdriver

class BrowserManager:
    def __init__(self):
        self.driver = None

    def start_browser(self, browser_name="chrome"):
        if browser_name == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_name == "firefox":
            self.driver = webdriver.Firefox()
        # Можно добавить другие браузеры
        else:
            raise ValueError(f"Browser {browser_name} is not supported")
        self.driver.maximize_window()
        return self.driver

    def quit_browser(self):
        if self.driver:
            self.driver.quit()
