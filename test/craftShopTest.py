from selenium import webdriver
from src.pages.landingPage import LandingPage
from src.pages.RegisterPage import RegisterPage

driver = webdriver.Chrome()
driver.get("http://shop.icraftsoft.net:8095/")

landing_page = LandingPage(driver)