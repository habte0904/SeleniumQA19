from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class LandingPage(PageFactory):
    def __int__(self, driver):
        self.driver = driver

    def getRegButton(self):
        return self.driver.findElement(By.XPATH, "//input[@value='Register']")