import time
from selenium.webdriver.common.by import By
from Atidstore.Locators.Test_women.women_locators import women_locators
from Atidstore.Test.BaseTest.Base import BaseTest


class Test_(BaseTest, women_locators):

    def test_check_women_page_displayed_or_not(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Women_page).click()
        time.sleep(2)
        women = driver.find_element(By.XPATH, self.Women_page).text
        assert women == "WOMEN"
        super().tear_down()

    def test_check_if_there_is_products_in_women_page(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Women_page).click()
        time.sleep(2)
        driver.execute_script(self.Scroll_down_1)
        time.sleep(2)
        driver.execute_script(self.Scroll_down_2)
        time.sleep(2)
        women = driver.find_element(By.XPATH, self.Women_page).text
        assert women == "WOMEN"
        super().tear_down()

    def test_check_if_showing_results_2_page_displayed(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Women_page).click()
        time.sleep(2)
        driver.execute_script(self.Scroll_down_1)
        time.sleep(2)
        driver.execute_script(self.Scroll_down_2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Women_2_page).click()
        women = driver.find_element(By.CLASS_NAME, self.page_numbers).text
        assert women == "←\n1\n2"
        super().tear_down()

    def test_check_if_sorting_button_sorts_products(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Women_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Women_Sorting_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Sort_by_popularity).click()
        time.sleep(2)
        sort = driver.find_element(By.XPATH, self.Sort_by_popularity).text
        assert sort == "Sort by popularity"
        super().tear_down()

    def test_check_if_the_products_are_selected(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Women_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Bright_gold_purse_with_chain).click()
        time.sleep(2)
        tshirt = driver.find_element(By.XPATH, self.tshirt).text
        assert tshirt == "Bright Gold Purse With Chain"
        super().tear_down()

    def test_check_if_the_products_are_added_to_cart(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Women_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Bright_gold_purse_with_chain).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        cart = driver.find_element(By.XPATH, self.Add_to_cart_button).text
        assert cart == "ADD TO CART"
        super().tear_down()
