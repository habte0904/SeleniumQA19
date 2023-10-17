import pytest
from selenium import webdriver


class pytestMethod:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()


    def testGoogleTitle(setup):
        setup.driver.get("https://www.google.com")
        print("Google title: " +setup.driver.title)

    def testIcraftShopTitle(setup):
        setup.driver.get("http://shop.icraftsoft.net:8095/")
        print("Google title: " + setup.driver.title)

