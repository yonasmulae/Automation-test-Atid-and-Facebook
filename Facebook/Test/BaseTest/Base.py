from selenium import webdriver


class BaseTest:
    driver = webdriver.Chrome()

    def init(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        self.driver.close()

