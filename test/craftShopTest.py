from selenium import webdriver
from src.pages.landingPage import LandingPage
from src.pages.RegisterPage import RegisterPage

import unittest


class craftShop(unittest.TestCase):

    def testCraftShop(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://shop.icraftsoft.net:8095/")

        lp = LandingPage(self.driver)
        lp.getRegButton()
