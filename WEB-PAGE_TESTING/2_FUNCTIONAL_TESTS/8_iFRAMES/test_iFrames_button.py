# imports
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.functional
def test_iFrame_button():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        xpath = '//a[contains(@href,"iframe")]'
        learn_more = '//a[@id="learn-more" and contains(@class, "btn-primary") and contains(text(), "Learn more")]'
        driver.find_element(By.XPATH, xpath).click()
        sleep(2)
        driver.find_element(By.XPATH, learn_more).click()
        sleep(2)
    except Exception as e:
        print("Error code:", e)
    finally:
        driver.quit()