from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Импортируем страницы
from home_page import HomePage

driver = webdriver.Chrome()

try:
    home_page = HomePage(driver)
    home_page.click_get_app()

    print("Test Passed.")

except NoSuchElementException:
    print("Test Failed: Element not found.")
except Exception as e:
    print(f"Test Failed: {e}")

finally:
    input("press to exit")
    driver.quit()
