from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegPage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def getUsername(self):
        try:
            username = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
            )
            assert username.is_displayed(), "username input is not displayed on the page."
            username.send_keys("qa19")

        except Exception as e:
            print(f"Assertion failed: {e}")

    def getEmail(self):
        try:
            email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
            )
            assert email.is_displayed(), "Email input is not displayed on the page."
            email.send_keys("qa19@gmail.com")

        except Exception as e:
            print(f"Assertion failed: {e}")

    def getButton(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@value="Register"]'))
            )
            assert button.is_displayed(), "username input is not displayed on the page."
            button.click()

        except Exception as e:
            print(f"Assertion failed: {e}")
