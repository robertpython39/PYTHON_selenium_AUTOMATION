# imports
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

##### TESTS #####

@pytest.mark.html
def test_open_browser():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
    except Exception as e:
        print("Error code:", e)



@pytest.mark.html
def test_maximize_welcomeScreen():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        time.sleep(5)
        driver.maximize_window()
        welcomeXpath = '//h1[@class="display-4" and text()="Welcome!"]'
        driver.find_element(By.XPATH, welcomeXpath)
    except Exception as e:
        print("Error code:", e)
    finally:
        driver.quit()





