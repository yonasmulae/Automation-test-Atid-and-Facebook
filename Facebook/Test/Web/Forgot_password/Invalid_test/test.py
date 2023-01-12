import time
from selenium.webdriver.common.by import By
from Facebook.Locators.Test_forgot_password.locators import Forgot_password
from Facebook.Test.BaseTest.Base import BaseTest


class Test_forgot_password(BaseTest, Forgot_password):

    def test_the_forget_password_functionality_with_invalid_email_address(self):
        driver = super().init()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Forget_password_selector).click()
        time.sleep(3)
        user_name = driver.find_element(By.ID, self.Forget_password_user_name_selector)
        user_name.send_keys(self.Invalid_email)
        driver.find_element(By.ID, self.Forget_password_search).click()
        time.sleep(5)
        forgot_password = driver.find_element(By.XPATH, self.assert_forget_password).text
        assert forgot_password == "Find Your Account"
        super().tear_down()

    def test_the_forget_password_functionality_with_empty_email_address(self):
        driver = super().init()
        time.sleep(2)
        driver.find_element(By.XPATH, self.Forget_password_selector).click()
        time.sleep(3)
        user_name = driver.find_element(By.ID, self.Forget_password_user_name_selector)
        user_name.send_keys(self.User_name_empty_text)
        driver.find_element(By.ID, self.Forget_password_search).click()
        time.sleep(5)
        forgot_password = driver.find_element(By.XPATH, self.assert_forget_password).text
        assert forgot_password == "Find Your Account"
        super().tear_down()

    def test_check_that_the_user_is_shown_confirmation_message(self):
        driver = super().init()
        time.sleep(2)
        driver.find_element(By.XPATH, ).click()
        time.sleep(3)
        user_name = driver.find_element(By.ID, self.Forget_password_user_name_selector)
        user_name.send_keys(self.User_name_text)
        driver.find_element(By.ID, self.Forget_password_search).click()
        time.sleep(5)
        super().tear_down()
