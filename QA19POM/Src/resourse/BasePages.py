from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element {locator} not found on the page.")
            return None

    def click(self, locator):
        element = self.wait_for_element(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
