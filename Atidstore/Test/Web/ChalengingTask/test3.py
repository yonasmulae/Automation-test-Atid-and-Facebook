import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Atidstore.Locators.ChalengingTask.locators import ChalengingTask_locators
from Atidstore.Test.BaseTest.Base import BaseTest


class Test(BaseTest, ChalengingTask_locators):

    def test_the_product_with_sale_the_original_price_greater_than_72(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        UL = driver.find_element(By.XPATH, self.nav_ul_our_bestseller)
        LI = UL.find_elements(By.TAG_NAME, self.nav_li_our_best_seller)

        for x in LI:
            rating = self.is_element_exist("rating", x)
            if rating == '5.00':
                print('yooooooooo')
                time.sleep(5)
                x.click()
                time.sleep(5)
                break
        super().tear_down()

    def is_element_exist(self, text, webElement):
        try:
            return webElement.find_element(By.CLASS_NAME, text).text
        except NoSuchElementException:
            return ''


