from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class ResultPage(BasePage):
    #Elements on ResultPage
    RESULTS_QUANTITY = (By.ID, "result-stats")

    def __init__(self, driver):
        super().__init__(driver)

    ##action methods

    ##this method click on results by title
    def click_on_result_by_title(self, title):
        self.find_element(By.XPATH, "(//span[contains(text(), '{}')]//ancestor::a)[1]".format(title)).click()

    def get_results_quantity(self):
        return self.find_element(*self.RESULTS_QUANTITY)