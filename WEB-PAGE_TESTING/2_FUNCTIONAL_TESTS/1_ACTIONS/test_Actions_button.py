# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_click_Actions():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        xpath = '//a[text()="Actions"]'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        driver.quit()
    except Exception as e:
        print("Error code:", e)

