from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class HomePage(BasePage):
    #Elements on HomePage
    SEARCH_BAR = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def __init__(self, driver):
        super().__init__(driver)

    ##action methods
    def fill_search_bar(self, value):
        self.find_element(*self.SEARCH_BAR).send_keys(value)

    def click_google_search_button(self):
        self.click_on_element(*self.SEARCH_BUTTON)

    def list_box_is_displayed(self):
        return self.element_is_displayed(*(By.XPATH, "//ul[@role='listbox']"))

    def click_on_element_of_list_box(self, position):
        self.find_element(*(By.XPATH, "(//ul[@role='listbox']//li)[{}]".format(position))).click()