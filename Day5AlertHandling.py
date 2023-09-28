import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializing browser and visit the site
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# type name in the input
driver.find_element(By.XPATH, "//input[contains(@id,'name')]").send_keys("Abebe")

# first click Alert button
alert = driver.find_element(By.XPATH, "//input[@id='alertbtn']")
alert.click()

# switch to alert page
time.sleep(2)
switch = driver.switch_to.alert

# display message on alert on the console
print(switch.text)
switch.accept()

