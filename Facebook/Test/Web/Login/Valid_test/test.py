import time
from selenium.webdriver.common.by import By
from Facebook.Locators.Test_login.locators import Login_locator
from Facebook.Test.BaseTest.Base import BaseTest


class Test(BaseTest, Login_locator):

    def test_login_with_user_and_password_correctly(self):
        driver = super().init()
        time.sleep(3)
        email = driver.find_element(By.CSS_SELECTOR, self.Css_selector_email)
        email.clear()
        time.sleep(3)
        email.send_keys(self.User_name_text)
        time.sleep(3)
        password = driver.find_element(By.CSS_SELECTOR, self.CSS_selector_password)
        password.clear()
        time.sleep(3)
        password.send_keys(self.Password_text)
        time.sleep(3)
        driver.find_element(By.XPATH, self.selector_login_button).click()
        login = driver.find_element(By.XPATH, self.assert_locator).text
        assert login == "QA Tester Yonas"
        super().tear_down()
        
