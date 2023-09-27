import time

from selenium import webdriver

driver = webdriver.Chrome()

# visit rahulshetty website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
time.sleep(3)

# visit google website
driver.get("https://www.google.com")
print(driver.title)
time.sleep(3)

# navigate
driver.back()
time.sleep(3)
print("After back navigate =" + driver.title)

driver.forward()
time.sleep(3)
print("After forward navigate =" + driver.title)
