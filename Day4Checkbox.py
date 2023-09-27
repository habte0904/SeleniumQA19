import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window() # to control our window

checkbox1 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']")
checkbox2 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']")
checkbox3 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']")

print(checkbox1.is_selected())

# click to be select first checkbox
checkbox1.click()
time.sleep(2)
print(checkbox1.is_selected())

# unselect
checkbox1.click()
time.sleep(2)
print(checkbox1.is_selected())
