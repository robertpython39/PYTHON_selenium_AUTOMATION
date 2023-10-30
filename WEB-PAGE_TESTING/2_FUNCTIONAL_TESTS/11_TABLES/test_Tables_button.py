# imports
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.functional
def test_loader():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        sleep(5)
        xpath = '//a[contains(@href,"web-table")]'
        driver.find_element(By.XPATH,xpath).click()
        sleep(7)
    except Exception as e:
        print(f"Error code: {e}")
    finally:
        driver.quit()