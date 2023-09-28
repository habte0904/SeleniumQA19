import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize browser
driver = webdriver.Chrome()
driver.get("https://www.busbud.com/en")
driver.maximize_window()

# find calendar
outboundDate = driver.find_element(By.XPATH, "//input[@id='outbound-date-input']")
returnDate = driver.find_element(By.XPATH, "//input[@id='return-date-input']")

outboundDate.click()
time.sleep(2)
outboundDate.send_keys("Sat, Sep 30")
outboundDate.is_displayed()

time.sleep(2)
returnDate.send_keys("Mon, Oct 2")
returnDate.is_displayed()

