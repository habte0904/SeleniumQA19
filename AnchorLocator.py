import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

# both link text and partial link text
# Link text locator
print(driver.current_url)
#driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# partial link text locator
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot password").click()
time.sleep(2)
print(driver.current_url)