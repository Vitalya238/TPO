from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.reddit.com/")

    wait = WebDriverWait(driver, 10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    user_agreement_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "User Agreement"))
    )

    user_agreement_button.click()

    wait.until(EC.url_contains("user-agreement"))

    print("Test Passed.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    input("press enter to exit")
    driver.quit()
