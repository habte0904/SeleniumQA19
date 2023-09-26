import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
# class name locator
#driver.find_element(By.CLASS_NAME, "inputtext").send_keys("abebe@gmail.com")

# css selector
driver.find_element(By.CSS_SELECTOR, "input[data-testid='royal_email']").send_keys("hello@gmail.com")
time.sleep(2)

# ID locator
driver.find_element(By.ID, "pass").send_keys("abebe123")
time.sleep(2)

# name locator
print(driver.current_url)
#driver.find_element(By.NAME, "login").click()
driver.find_element(By.XPATH, "//button[@name='login']").click()
print(driver.current_url)

time.sleep(2)



