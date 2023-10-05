import unittest
from selenium import webdriver


class BrowserTitle(unittest.TestCase):

    def googleTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        self.driver.close()

    def rahelShetTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")


