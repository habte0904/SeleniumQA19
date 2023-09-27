import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window() # to control our window

s = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))

# select by value
s.select_by_value("option2")
time.sleep(3)

# select by index
s.select_by_index(3)
time.sleep(3)

# select by visible text
s.select_by_visible_text("Option1")
time.sleep(3)

