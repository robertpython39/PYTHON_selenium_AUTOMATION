# imports
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.functional
def test_dropdowns():
    try:
        driver = webdriver.Chrome()
        driver.get(url = 'https://qa-automation-practice.netlify.app/')
        driver.maximize_window()
        xpath = '//a[contains(@id,"dropdowns")]'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(5)
    except Exception as e:
        print("Error code:", e)
    finally:
        driver.quit()