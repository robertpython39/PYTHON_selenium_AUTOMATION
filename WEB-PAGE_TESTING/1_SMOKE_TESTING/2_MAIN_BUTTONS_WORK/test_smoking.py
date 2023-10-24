# imports
import time
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

##### TESTS #####

@pytest.mark.html
def test_open_web_browser():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        time.sleep(2)
    except Exception as e:
        print("Error code:", e)
    finally:
        driver.quit()

@pytest.mark.html
def test_maximize_web_browser_window():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        time.sleep(10)
    except Exception as e:
        print("Error code:", e)
    finally:
        driver.quit()

@pytest.mark.html
def test_make_request():
    try:
        response = requests.get(url="https://qa-automation-practice.netlify.app/")
        assert response.status_code == 200
    except Exception as e:
        print("Error code:", e)



