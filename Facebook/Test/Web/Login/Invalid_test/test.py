import time
from selenium.webdriver.common.by import By
from Facebook.Locators.Test_login.locators import Login_locator
from Facebook.Test.BaseTest.Base import BaseTest


class Test(BaseTest, Login_locator):

    def test_login_incorrectly_when_user_name_null(self):
        driver = super().init()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.Css_selector_email).send_keys(self.User_name_empty_text)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).send_keys(self.Password_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.selector_login_button).click()
        time.sleep(3)
        login = driver.find_element(By.XPATH, self.assert_locator).text
        assert login == "Log in to Facebook"
        super().tear_down()

    def test_login_incorrectly_when_password_null(self):
        driver = super().init()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.Css_selector_email).send_keys(self.User_name_text)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).send_keys(self.Password_empty_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.selector_login_button).click()
        time.sleep(3)
        login = driver.find_element(By.XPATH, self.assert_locator_2).text
        assert login == "Log in as QA Tester Yonas"
        super().tear_down()

    def test_login_incorrectly_when_username_and_password_null(self):
        driver = super().init()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.Css_selector_email).send_keys(self.User_name_empty_text)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).send_keys(self.Password_empty_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.selector_login_button).click()
        time.sleep(8)
        login = driver.find_element(By.XPATH, self.assert_locator_3).text
        assert login == "Log in to Facebook"
        super().tear_down()

    def test_login_incorrectly_when_password_caracters_lessthan_4(self):
        driver = super().init()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.Css_selector_email).send_keys(self.User_name_text)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).send_keys(self.Password_less_than_4_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.selector_login_button).click()
        time.sleep(3)
        login = driver.find_element(By.XPATH, self.assert_locator_2).text
        assert login == "Log in as QA Tester Yonas"
        super().tear_down()

    def test_check_the_password_is_displayed_in_the_form_of_Asterisk(self):
        driver = super().init()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.Css_selector_email).send_keys(self.User_name_text)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).send_keys(self.Password_text)
        time.sleep(3)
        password = driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).text
        assert password == ""
        super().tear_down()

    def test_check_Errors_are_handled_properly_or_return_an_error_message_for_any_query(self):
        driver = super().init()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.Css_selector_email).send_keys(self.User_name_empty_text)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password).send_keys(self.Password_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.selector_login_button).click()
        time.sleep(3)
        login = driver.find_element(By.XPATH, self.assert_locator_3).text
        assert login == "Log in to Facebook"
        super().tear_down()

