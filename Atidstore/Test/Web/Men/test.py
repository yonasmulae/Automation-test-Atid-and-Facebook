import time
from selenium.webdriver.common.by import By
from Atidstore.Locators.Test_men.men_locators import men_locators
from Atidstore.Test.BaseTest.Base import BaseTest


class Test(BaseTest, men_locators):

    def test_check_men_page_displayed_or_not(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Men_page).click()
        time.sleep(2)
        men = driver.find_element(By.XPATH, self.Men_page).text
        assert men == "MEN"
        super().tear_down()

    def test_check_if_there_is_products_in_men_page(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Men_page).click()
        time.sleep(2)
        men = driver.find_element(By.XPATH, self.Men_page).text
        assert men == "MEN"
        super().tear_down()

    def test_check_if_showing_results_2_page_displayed(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Men_page).click()
        time.sleep(2)
        driver.execute_script(self.Scroll_down_1)
        time.sleep(2)
        driver.execute_script(self.Scroll_down_2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Men_2_page).click()
        second_page = driver.find_element(By.CLASS_NAME, self.page_numbers).text
        assert second_page == "←\n1\n2"
        super().tear_down()


    def test_check_if_sorting_button_sorts_products(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Men_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Men_Sorting_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Sort_by_popularity).click()
        time.sleep(2)
        sort = driver.find_element(By.XPATH, self.Sort_by_popularity).text
        assert sort == "Sort by popularity"
        super().tear_down()

    def test_check_if_the_products_are_selected(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Men_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Black_hoodie).click()
        time.sleep(2)
        tshirt = driver.find_element(By.XPATH, self.tshirt).text
        assert tshirt == "Black Hoodie"
        super().tear_down()

    def test_check_if_the_products_are_added_to_cart(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Men_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Black_hoodie).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        cart = driver.find_element(By.XPATH, self.Add_to_cart_button).text
        assert cart == "ADD TO CART"
        super().tear_down()
