from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver, base_url="http://www.google.com"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 20
        self.implicit_wait = 10

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def click_on_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, self.implicit_wait).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutError:
            raise

    def get_title(self):
        return self.driver.title

    def title_match(self, value):
        wait = WebDriverWait(self, self.implicit_wait)
        message = 'Timeout waiting for title to be \'{}\''.format(value)
        return wait.until(EC.title_is(value), message=message)

    def element_is_displayed(self, *locator):
        try:
            element = WebDriverWait(self.driver, self.implicit_wait).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutError:
            raise
