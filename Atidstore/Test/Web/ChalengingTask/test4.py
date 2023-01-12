import time
from selenium.webdriver.common.by import By
from Atidstore.Locators.ChalengingTask.locators import ChalengingTask_locators
from Atidstore.Test.BaseTest.Base import BaseTest


class Test(BaseTest, ChalengingTask_locators):

    def test_Send_Question_to_the_site_admin_via_Contact_Us(self):
        driver = super().init()
        driver.find_element(By.XPATH, self.Contact_us_page).click()
        time.sleep(3)
        name_text = driver.find_element(By.CSS_SELECTOR, self.Css_selector_name)
        name_text.clear()
        time.sleep(3)
        name_text.send_keys(self.Input_text_for_name)
        name_text = driver.find_element(By.CSS_SELECTOR, self.Css_selector_subject)
        name_text.clear()
        time.sleep(3)
        name_text.send_keys(self.Input_text_for_subject)
        time.sleep(3)
        name_text = driver.find_element(By.CSS_SELECTOR, self.Css_selector_email)
        name_text.clear()
        time.sleep(3)
        name_text.send_keys(self.Input_text_for_email)
        time.sleep(3)
        name_text = driver.find_element(By.CSS_SELECTOR, self.Css_selector_message)
        name_text.clear()
        time.sleep(3)
        name_text.send_keys(self.Input_text_for_message)
        time.sleep(3)
        send_message = driver.find_element(By.XPATH, self.Send_messgae_button).click()
        assert send_message == "Send Message"
        super().tear_down()

