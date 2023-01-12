import time
from selenium.webdriver.common.by import By
from Atidstore.Locators.Scroll_down.Scroll_down_locator import Scroll_down
from Atidstore.Test.BaseTest.Base import BaseTest


class Test(BaseTest, Scroll_down):

    def test_check_if_showing_results_3_page_displayed(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        driver.execute_script(self.Scroll_down_1)
        time.sleep(2)
        driver.execute_script(self.Scroll_down_2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Store_3_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Green_hoodie).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart).click()
        time.sleep(2)
        add_to_cart = driver.find_element(By.XPATH, self.Add_to_cart).text
        assert add_to_cart == "ADD TO CART"



