# imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

##### TESTS #####
@given('Open "{url}"')
def step_open_browser(context, url):
    try:
        context.driver = webdriver.Chrome()
        context.driver.get(url)
        context.driver.maximize_window()
    except Exception as e:
        assert "Check webdriver for your browser and run the test again"

    return

@then('Target "{text}" link')
def step_target_Cypress(context, text):
    try:
        xpath_link = '(//em[contains(text(),"CLICK HERE")])[1]'
        xpath_text = f'(//h4[text()="{text}"]'
        if context.driver.find_element(By.XPATH, xpath_text):
            link_element = context.driver.find_element(By.XPATH, xpath_link)
            link_element.send_keys(Keys.ENTER)

    except Exception as e:
        assert "Link is not working. Check xPath"
    return

@then('Target "{TestCafe}" link')
def step_target_TestCafe(context, text):
    try:
        xpath_link = '(//em[contains(text(),"CLICK HERE")])[2]'
        xpath_text = f'(//h4[text()="{text}"]'
        if context.driver.find_element(By.XPATH, xpath_text):
            link_element = context.driver.find_element(By.XPATH, xpath_link)
            link_element.click()

    except Exception as e:
        assert "Link is not working. Check xPath"
    return context.driver.quit()

@then('Target "{API_Automation}" link')
def step_target_API_Automation(context, text):
    try:
        xpath_link = '(//em[contains(text(),"CLICK HERE")])[3]'
        xpath_text = f'(//h4[text()="{text}"]'
        if context.driver.find_element(By.XPATH, xpath_text):
            link_element = context.driver.find_element(By.XPATH, xpath_link)
            link_element.click()

    except Exception as e:
        assert "Link is not working. Check xPath"
    return context.driver.quit()
time.sleep(5)