from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LandingPage:
    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def getRegButton(self):
        return self.driver.find_element(By.XPATH, "//input[@value='Register']")
