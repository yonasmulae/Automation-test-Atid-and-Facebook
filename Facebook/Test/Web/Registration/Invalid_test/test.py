import time
from selenium.webdriver.common.by import By
from Facebook.Locators.Test_regestration.locators import Regestration_locator
from Facebook.Test.BaseTest.Base import BaseTest


class Test_login(BaseTest, Regestration_locator):

    def test_Check_the_error_signup_by_entering_invalid_data_in_all_the_mandatory_fields(self):
        driver = super().init()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Create_new_account).click()
        time.sleep(3)
        driver.find_element(By.NAME, self.First_name_selector).send_keys(self.First_name)
        time.sleep(3)
        driver.find_element(By.NAME, self.Last_name_selector).send_keys(self.Last_name)
        time.sleep(3)
        driver.find_element(By.NAME, self.Email_selector).send_keys(self.Email)
        time.sleep(3)
        driver.find_element(By.NAME, self.Re_enter_user_name).send_keys(self.Re_enter_email)
        time.sleep(3)
        driver.find_element(By.NAME, self.New_password_selector).send_keys(self.Password)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_date_selector).send_keys(self.Birth_date_date)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_month_selecter).send_keys(self.Birth_date_month)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_year_selector).send_keys(self.Birth_date_year)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Gender_male).click()
        time.sleep(3)
        driver.find_element(By.NAME, self.Sign_up_button).click()
        time.sleep(3)
        sign_up = driver.find_element(By.NAME, self.Sign_up_button).text
        assert sign_up == "Sign Up"
        super().tear_down()

    def test_Check_the_registration_page_without_entering_any_data_in_fields(self):
        driver = super().init()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Create_new_account).click()
        time.sleep(3)
        driver.find_element(By.NAME, self.First_name_selector).send_keys(self.Empty_first_name)
        time.sleep(3)
        driver.find_element(By.NAME, self.Last_name_selector).send_keys(self.Empty_last_name)
        time.sleep(3)
        driver.find_element(By.NAME, self.Email_selector).send_keys(self.Empty_email)
        time.sleep(3)
        driver.find_element(By.NAME, self.Re_enter_user_name).send_keys(self.Empty_re_enter_email)
        time.sleep(3)
        driver.find_element(By.NAME, self.New_password_selector).send_keys(self.Empty_password)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_date_selector).send_keys(self.Empty_birt_date_date)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_month_selecter).send_keys(self.Empty_birth_date_month)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_year_selector).send_keys(self.Empty_birth_date_year)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Gender_male).click()
        time.sleep(3)
        driver.find_element(By.NAME, self.Sign_up_button).click()
        time.sleep(3)
        sign_up = driver.find_element(By.NAME, self.Sign_up_button).text
        assert sign_up == "Sign Up"
        super().tear_down()

    def test_Check_the_confirmation_message_when_the_user_is_successfully_signup_or_registered(self):
        driver = super().init()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Create_new_account).click()
        time.sleep(3)
        driver.find_element(By.NAME, self.First_name_selector).send_keys(self.First_name)
        time.sleep(3)
        driver.find_element(By.NAME, self.Last_name_selector).send_keys(self.Last_name)
        time.sleep(3)
        driver.find_element(By.NAME, self.Email_selector).send_keys(self.Email)
        time.sleep(3)
        driver.find_element(By.NAME, self.Re_enter_user_name).send_keys(self.Re_enter_email)
        time.sleep(3)
        driver.find_element(By.NAME, self.New_password_selector).send_keys(self.Password)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_date_selector).send_keys(self.Birth_date_date)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_month_selecter).send_keys(self.Birth_date_month)
        time.sleep(3)
        driver.find_element(By.NAME, self.Birth_date_year_selector).send_keys(self.Birth_date_year)
        time.sleep(3)
        driver.find_element(By.XPATH, self.Gender_male).click()
        time.sleep(3)
        driver.find_element(By.NAME, self.Sign_up_button).click()
        time.sleep(3)
        sign_up = driver.find_element(By.NAME, self.Sign_up_button).text
        assert sign_up == "Sign Up"
        super().tear_down()

