from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class RegisterPage(PageFactory):
    def __int__(self, driver):
        self.driver = driver

    def getUserName(self):
        return self.driver.findElement(By.XPATH, "//input[@name='username']")

    def getEmail(self):
        return self.driver.findElement(By.XPATH, "//input[@name='email']")

    def getButton(self):
        return self.driver.findElement(By.XPATH, "//input[@class='btnSubmit']")
