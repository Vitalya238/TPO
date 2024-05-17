from selenium import webdriver

from home_page import HomePage
from user_agreement_page import UserAgreementPage

driver = webdriver.Chrome()

try:
    home_page = HomePage(driver)
    home_page.scroll_to_bottom()
    home_page.click_user_agreement()

    user_agreement_page = UserAgreementPage(driver)

    print("Test Passed.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    input("press enter to exit")
    driver.quit()
