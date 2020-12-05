from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")

    context.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


def after_all(context):
    context.browser.quit()
