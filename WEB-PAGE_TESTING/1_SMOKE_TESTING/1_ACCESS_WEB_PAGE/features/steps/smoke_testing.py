# imports
import time
import requests
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

##### TESTS #####

@given('Open web browser "{url}"')
def step_open_web_browser(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@when('Maximize the web browser window')
def step_maximize_web_browser_window(context):
    context.driver.maximize_window()
    time.sleep(10)

@given('Make request to "{url}"')
def step_make_request(context, url):
    context.response = requests.get(url)

@when('Request is 200')
def step_request_is_200(context):
    assert context.response.status_code == 200

@then('I close the browser window')
def step_close_browser_window(context):

    context.driver.quit()


