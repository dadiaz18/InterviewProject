from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.home_page import HomePage
from features.pages.result_page import ResultPage

"""
 the references of pages will be in context.scenario
 example context.scenario.name_of_page to have reference in all steps
"""

@step(u"I'm on the homepage")
def step_impl(context):
    context.scenario.home_page = HomePage(context.browser)
    context.scenario.home_page.open("/")

@step(u'I type "{item}" into the search field')
def step_impl(context, item):
    context.scenario.home_page.fill_search_bar(item)

@step(u'I click the Google Search button')
def step_impl(context):
    context.scenario.home_page.click_google_search_button()
    context.scenario.result_page = ResultPage(context.browser)

@step(u'I click on "{item}" result')
def step_impl(context, item):
    context.scenario.result_page.click_on_result_by_title(item)

@step(u'I go to the "{item}" page')
def step_impl(context, item):
    if item.lower() == "search results":
        assert context.scenario.result_page.get_results_quantity().is_displayed()
    else:
        wait = WebDriverWait(driver=context.browser, timeout=10)
        message = 'Timeout waiting for title to be \'{}\''.format(item)
        assert wait.until(EC.title_is(item), message=message)


@step(u'the suggestions list is displayed')
def step_impl(context):
    assert context.scenario.home_page.list_box_is_displayed()

@step(u'I click on the first suggestion in the list')
def step_impl(context):
    context.scenario.home_page.click_on_element_of_list_box(1)
    context.scenario.result_page = ResultPage(context.browser)