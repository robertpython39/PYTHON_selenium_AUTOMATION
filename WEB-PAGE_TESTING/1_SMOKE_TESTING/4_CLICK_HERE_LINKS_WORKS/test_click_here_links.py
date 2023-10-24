# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

##### TESTS #####

def test_target_Cypress():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        xpath_link = '(//em[contains(text(),"CLICK HERE")])[1]'
        xpath_text = '//h4[text()="Cypress Framework Tutorials - From Zero to Hero"]'
        if driver.find_element(By.XPATH, xpath_text):
            link_element = driver.find_element(By.XPATH, xpath_link)
            link_element.click()
            time.sleep(2)
            driver.quit()
    except Exception as e:
            print("Error code:", e)


def test_target_TestCafe():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        xpath_link = '(//em[contains(text(),"CLICK HERE")])[2]'
        xpath_text = '//h4[text()="TestCafe Framework Tutorials - Web E2E - From Zero to Hero"]'
        if driver.find_element(By.XPATH, xpath_text):
            link_element = driver.find_element(By.XPATH, xpath_link)
            link_element.click()
            time.sleep(2)
            driver.quit()
    except Exception as e:
            print("Error code:", e)

def test_target_API_Automation():
    try:
        driver = webdriver.Chrome()
        driver.get(url="https://qa-automation-practice.netlify.app/")
        driver.maximize_window()
        xpath_link = '(//em[contains(text(),"CLICK HERE")])[3]'
        xpath_text = '//h4[text()="API Automation Tutorials - Getting started with PactumJS"]'
        if driver.find_element(By.XPATH, xpath_text):
            link_element = driver.find_element(By.XPATH, xpath_link)
            link_element.click()
            time.sleep(2)
            driver.quit()
    except Exception as e:
            print("Error code:", e)
