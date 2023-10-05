import unittest
from selenium import webdriver


class BrowserTitle(unittest.TestCase):

    def test_googleTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        self.driver.close()

    def test_rahelShetTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


