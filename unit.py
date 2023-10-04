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

# outbound date
outbound = driver.find_element(By.XPATH, "//input[@id='outbound-date-input']")
outbound.click()
time.sleep(2)
button1 = driver.find_element(By.XPATH, "//button[@data-date='2023-10-18']")
button1.click()
time.sleep(2)

# return date
returndate = driver.find_element(By.XPATH, "//input[@id='return-date-input']")
returndate.click()
time.sleep(2)
next = driver.find_element(By.XPATH, "//button[@aria-label='Next month']")
next.click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@data-date='2023-11-08']").click()
time.sleep(3)

# passenger
passenger = driver.find_element(By.XPATH, "//input[contains(@id,'passenger-input')]")
passenger.click()
time.sleep(2)

adult = driver.find_element(By.XPATH, "//button[@data-testid='adult-increment']")
i = 0
while i<3:
    adult.click()
    i = i+1
time.sleep(3)

# search button
search = driver.find_element(By.XPATH, "//div[@id='search-submit-button']")
search.click()


