import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.busbud.com/")
driver.maximize_window()

# origin
origin = driver.find_element(By.XPATH, "//input[@id='origin-c1ty-input']")
origin.send_keys("new")
time.sleep(2)
origin.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# destination
d = driver.find_element(By.XPATH, "//input[@id='destination-c1ty-input']")
d.send_keys("wash")
time.sleep(2)
d.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
