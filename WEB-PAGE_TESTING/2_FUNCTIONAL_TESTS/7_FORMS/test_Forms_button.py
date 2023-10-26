# imports
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.functional
def test_forms():
    try:
        driver = webdriver.Chrome()
        driver.get(url='https://qa-automation-practice.netlify.app/')
        driver.maximize_window()
        time.sleep(3)
        xpath = '//a[contains(@id,"forms")]'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(5)
    except Exception as e:
        print("Error code:\n", e)
    finally:
        driver.minimize_window()
        driver.quit()