# Selenium testing tutorial to automate calendar using Selenium WebDriver inside an iFrame.
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# The Date Range picker is from https://jqueryui.com/datepicker/#date-range

expected_from_date_str = '01/20/2020'
expected_to_date_str = '02/26/2020'

expected_fr_date = '20'
expected_to_date = '26'

test_url = 'https://jqueryui.com/datepicker/#date-range'


class CalendarControlTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_calendar_control_range_(self):
        driver = self.driver
        driver.get(test_url)
        time.sleep(5)

        frame = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
        driver.switch_to.frame(frame)

        ################################# Steps for the From Date ############################
        from_dp = driver.find_element(By.XPATH, "//input[@id='from']")
        from_dp.click()
        time.sleep(5)

        from_month = driver.find_element(By.XPATH, "//div/select[@class='ui-datepicker-month']")
        selected_from_month = Select(from_month)
        selected_from_month.select_by_visible_text("Jan")
        time.sleep(5)

        # from_day = driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='20']")
        from_day = driver.find_element(By.XPATH, "//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + expected_fr_date + "']")
        from_day.click()
        time.sleep(10)

        ################################# Steps for the To Date ############################
        # The same steps like the ones in From Month are repeated except that now the operations
        # are performed on a different web element.

        to_dp = driver.find_element(By.XPATH, "//input[@id='to']")
        to_dp.click()
        time.sleep(5)

        to_month = driver.find_element(By.XPATH, "//div/select[@class='ui-datepicker-month']")
        selected_to_month = Select(to_month)
        selected_to_month.select_by_visible_text("Feb")
        time.sleep(5)

        # day_to=driver.find_element_by_xpath("//table/tbody/tr/td/a[text()='26']")
        to_day = driver.find_element(By.XPATH, "//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + expected_to_date + "']")
        to_day.click()
        time.sleep(10)

        ################################# Verify whether the values are as expected ############################
        selected_from_date_str = from_dp.get_attribute('value')
        self.assertEqual(selected_from_date_str, expected_from_date_str)

        selected_to_date_str = to_dp.get_attribute('value')
        self.assertEqual(selected_to_date_str, expected_to_date_str)

        print("Unit Test of jQuery Calendar passed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
