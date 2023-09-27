import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window() # to control our window

d = driver.find_element(By.XPATH, "//input[@id='autocomplete']")
d.send_keys("eth")
time.sleep(3)
d.send_keys(Keys.ARROW_DOWN)
d.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
d.send_keys(Keys.ENTER)

time.sleep(3)
