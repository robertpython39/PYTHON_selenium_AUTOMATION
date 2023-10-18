# FUNCTIONAL TESTS
import time

# imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Open web browser "{url}"')
def step_open_web_browser(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@when('Maximize the web browser window')
def step_maximize_web_browser_window(context):
    context.driver.maximize_window()
    time.sleep(10)

@then('Welcome screen should be "{expected_text}"')
def step_check_welcome_screen(context, expected_text):
    xpath = "//h1[@class='display-4' and contains(text(),'Welcome!')]"
    actual_text = context.driver.find_element(By.XPATH, xpath)
    assert actual_text , f"Expected text: Actual text: {actual_text}"

@when('I close the browser window')
def step_close_browser_window(context):
    context.driver.quit()


