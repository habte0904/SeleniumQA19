
# import
from selenium import webdriver  # to create object of webdriver we must import
from selenium.webdriver.common.keys import Keys

# first create webdriver object
driver = webdriver.Chrome()

# url visit
driver.get("https://www.google.com")


print(driver.title)        # return title of the page
print(driver.current_url)  # return current url of the visit site
print(driver.page_source)  # return source of the page

# to Close driver
driver.close()



