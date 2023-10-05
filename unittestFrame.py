import unittest
from selenium import webdriver


class unittestFramework(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        print("From Setup method")

    def tearDown(self) -> None:
        print(self.driver.title)
        self.driver.close()
        print("From TearDown method")

    @classmethod
    def setUpClass(cls) -> None:
        print("From setupclass method")

    @classmethod
    def tearDownClass(cls) -> None:
        print("From teardownclass method")

    # ====================
    # Test method
    # =====================
    def test_googleTitle(self):
        self.driver.get("https://www.google.com")

    def test_rahelShetTitle(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")


if __name__ == "__main__":
    unittest.main()
