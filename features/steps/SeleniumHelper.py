from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_till_element_is_present(self, locator, timeout=10):
        flag = False
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            flag = True
        except Exception as e:
            print(f"Exception occurred while checking for element presence: {e} ")
            return flag
