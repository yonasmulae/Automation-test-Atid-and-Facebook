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
        UL = driver.find_element(By.XPATH, self.NAV_UL_PRICE)
        LI = UL.find_elements(By.XPATH, self.NAV_LI_PRICE)

        for x in LI:
            price = x.find_element(By.XPATH, self.Price)
            sale = self.is_element_exist('onsale', x)
            if price.text == "120.00 ₪" and sale == 'Sale!':
                x.click()
                time.sleep(5)
                break
        super().tear_down()

    def is_element_exist(self, text, webElement):
        try:
            return webElement.find_element(By.CLASS_NAME, text).text
        except NoSuchElementException:
            return ''


