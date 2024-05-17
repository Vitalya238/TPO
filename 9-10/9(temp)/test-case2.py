
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

try:
    driver.get("https://www.reddit.com/")

    wait = WebDriverWait(driver, 10)

    get_app_button = wait.until(
        EC.element_to_be_clickable((By.ID, "get-app"))
    )

    try:
        get_app_button.click()
        print("Test Passed.")
    except NoSuchElementException:
        print("Test Failed.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    input("press to exit")
    driver.quit()
