import time
from selenium.webdriver.common.by import By
from Atidstore.Locators.ChalengingTask.locators import ChalengingTask_locators
from Atidstore.Test.BaseTest.Base import BaseTest


class Test(BaseTest, ChalengingTask_locators):

    def test_E2E_atid_green_tshirt(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Atid_green_tshirt).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.View_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_selector).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_first_name).send_keys(self.Check_out_first_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_last_name).send_keys(self.Check_out_last_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_company_name).send_keys(self.Check_out_company_name_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Check_out_billing_address).send_keys(self.Check_out_billing_address_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_billing_address2).send_keys(self.Check_out_billing_address_text2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_post_code).send_keys(self.Check_out_post_code_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_town).send_keys(self.Check_out_town_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_phone).send_keys(self.Check_out_phone_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_email_address).send_keys(self.Check_out_email_address_text)
        time.sleep(2)
        order = driver.find_element(By.XPATH, self.Place_order).text
        assert order == "PLACE ORDER"
        super().tear_down()

    def test_E2E_anchor_bracelet(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Anchor_Bracelet).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.View_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_selector).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_first_name).send_keys(self.Check_out_first_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_last_name).send_keys(self.Check_out_last_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_company_name).send_keys(self.Check_out_company_name_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Check_out_billing_address).send_keys(self.Check_out_billing_address_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_billing_address2).send_keys(self.Check_out_billing_address_text2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_post_code).send_keys(self.Check_out_post_code_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_town).send_keys(self.Check_out_town_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_phone).send_keys(self.Check_out_phone_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_email_address).send_keys(self.Check_out_email_address_text)
        time.sleep(2)
        order = driver.find_element(By.XPATH, self.Place_order).text
        assert order == "PLACE ORDER"
        super().tear_down()

    def test_E2E_black_hoodie(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Black_hoodie).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.View_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_selector).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_first_name).send_keys(self.Check_out_first_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_last_name).send_keys(self.Check_out_last_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_company_name).send_keys(self.Check_out_company_name_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Check_out_billing_address).send_keys(self.Check_out_billing_address_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_billing_address2).send_keys(self.Check_out_billing_address_text2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_post_code).send_keys(self.Check_out_post_code_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_town).send_keys(self.Check_out_town_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_phone).send_keys(self.Check_out_phone_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_email_address).send_keys(self.Check_out_email_address_text)
        time.sleep(2)
        order = driver.find_element(By.XPATH, self.Place_order).text
        assert order == "PLACE ORDER"
        super().tear_down()

    def test_E2E_bright_gold_purse_with_chain(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Bright_gold_purse_with_chain).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.View_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_selector).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_first_name).send_keys(self.Check_out_first_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_last_name).send_keys(self.Check_out_last_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_company_name).send_keys(self.Check_out_company_name_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Check_out_billing_address).send_keys(self.Check_out_billing_address_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_billing_address2).send_keys(self.Check_out_billing_address_text2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_post_code).send_keys(self.Check_out_post_code_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_town).send_keys(self.Check_out_town_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_phone).send_keys(self.Check_out_phone_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_email_address).send_keys(self.Check_out_email_address_text)
        time.sleep(2)
        order = driver.find_element(By.XPATH, self.Place_order).text
        assert order == "PLACE ORDER"
        super().tear_down()

    def test_E2E_blue_denim_jeans(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Store_page).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Blue_denim_jeans).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Add_to_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.View_cart_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_selector).click()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_first_name).send_keys(self.Check_out_first_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_last_name).send_keys(self.Check_out_last_name_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_company_name).send_keys(self.Check_out_company_name_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Check_out_billing_address).send_keys(self.Check_out_billing_address_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_billing_address2).send_keys(self.Check_out_billing_address_text2)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_post_code).send_keys(self.Check_out_post_code_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_town).send_keys(self.Check_out_town_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_phone).send_keys(self.Check_out_phone_text)
        time.sleep(2)
        driver.find_element(By.XPATH, self.Check_out_email_address).send_keys(self.Check_out_email_address_text)
        time.sleep(2)
        order = driver.find_element(By.XPATH, self.Place_order).text
        assert order == "PLACE ORDER"
        super().tear_down()