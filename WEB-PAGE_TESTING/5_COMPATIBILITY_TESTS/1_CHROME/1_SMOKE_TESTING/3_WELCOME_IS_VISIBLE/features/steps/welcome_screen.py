# imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

##### TESTS #####
@given('Open "{url}"')
def step_open_browser(context, url):
    try:
        context.driver = webdriver.Chrome()
        context.driver.get(url)
    except Exception as e:
        assert "Check webdriver for your browser and run the test again"

    return

@when('Maximize window and {text} is on the first page')
def step_maximize_welcomeScreen(context, text):
    try:
        context.driver.maximize_window()
        time.sleep(5)
        welcomeXpath = '//h1[contains(text(),{text}")]'
        context.driver.find_element(By.XPATH, welcomeXpath)
    except Exception as e:
        assert "Element not found!"

    return

@then('Close the browser')
def step_close_browser_window(context):
    context.driver.quit()
    return



