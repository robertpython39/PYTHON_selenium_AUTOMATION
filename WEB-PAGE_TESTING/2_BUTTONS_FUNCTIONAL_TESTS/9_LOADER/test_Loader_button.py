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
        xpath = '//a[contains(@href,"loader")]'
        driver.find_element(By.XPATH, xpath).click()
        sleep(10)
    except Exception as e:
        print(f"Error code {e}")
    finally:
        driver.quit()