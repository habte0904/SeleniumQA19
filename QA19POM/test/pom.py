import time

from selenium import webdriver

from Src.Pages.LandingPage import LandingPage
from Src.Pages.RegPage import RegPage

driver = webdriver.Chrome()
driver.get('http://shop.icraftsoft.net:8095/')


# Landing Page
lp = LandingPage(driver)  # object create
lp.click_login()
time.sleep(3)

# Register username and password
rg = RegPage(driver)
rg.getUsername()
rg.getEmail()
rg.getButton()

time.sleep(4)

