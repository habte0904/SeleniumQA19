import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.busbud.com/")
driver.maximize_window()  # used to maximize the browser


# origin city
origin = driver.find_element(By.XPATH, "//input[@id='origin-c1ty-input']")
origin.send_keys("new")
time.sleep(3)
origin.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
origin.send_keys(Keys.ENTER)

# Destination city
dest = driver.find_element(By.XPATH, "//input[@id='destination-c1ty-input']")
dest.send_keys("wash")
time.sleep(3)
dest.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
dest.send_keys(Keys.ENTER)
time.sleep(3)

# out bound date
outbound = driver.find_element(By.XPATH, "//input[@id='outbound-date-input']")
outbound.click()
time.sleep(3)
date = driver.find_element(By.XPATH, "//button[@data-date='2023-10-24']")
date.click()
time.sleep(3)

# return date
rdate = driver.find_element(By.XPATH, "//input[@id='return-date-input']")
rdate.click()
time.sleep(3)
nextpage = driver.find_element(By.XPATH, "//button[@data-next-month='true']")
nextpage.click()
time.sleep(3)
d = driver.find_element(By.XPATH, "//button[@data-date='2023-11-08']")
d.click()
time.sleep(3)

# passenger
pas = driver.find_element(By.XPATH, "//input[contains(@id,'passenger-input')]")
pas.click()
time.sleep(3)
adult = driver.find_element(By.XPATH, "//button[@data-testid='adult-increment']")
i = 0
while i < 2:
    adult.click()
    i = i + 1
time.sleep(3)

# remove passenger popup
driver.find_element(By.XPATH, "//html[contains(@lang,'en')]").click()
time.sleep(3)

# click search button
driver.find_element(By.XPATH, "//div[contains(@id,'search-submit-button')]").click()
time.sleep(5)
