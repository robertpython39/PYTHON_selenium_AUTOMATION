import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.functional
class TestButtonsDropdown:

    xpaths = ['//a[text()="Buttons"]',
              '//a[text()="Checkboxes"]'
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_1_Radio_buttons(self):
        buttons_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        buttons_dropdown.click()
        sleep(5)
        if buttons_dropdown:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            for i in range(3):
                self.driver.find_element(By.XPATH, '//input[contains(@id, "checkbox1")]').click()
                sleep(2)
                reset_button = self.driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-primary")]')
                reset_button.click()
                sleep(4)

    def test_2_Radio_buttons(self):
        buttons_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        buttons_dropdown.click()
        sleep(5)
        if buttons_dropdown:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            for i in range(3):
                self.driver.find_element(By.XPATH, '//input[contains(@id, "checkbox1")]').click()
                sleep(2)
                self.driver.find_element(By.XPATH, '//input[contains(@id, "checkbox2")]').click()
                sleep(2)
                reset_button = self.driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-primary")]')
                reset_button.click()
                sleep(4)

    def test_3_Radio_buttons(self):
        buttons_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        buttons_dropdown.click()
        sleep(5)
        if buttons_dropdown:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            for i in range(3):
                self.driver.find_element(By.XPATH, '//input[contains(@id, "checkbox1")]').click()
                sleep(2)
                self.driver.find_element(By.XPATH, '//input[contains(@id, "checkbox2")]').click()
                sleep(2)
                self.driver.find_element(By.XPATH, '//input[contains(@id, "checkbox3")]').click()
                sleep(2)
                reset_button = self.driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-primary")]')
                reset_button.click()
                sleep(4)

    def test_2random_Radio_buttons(self):
        buttons_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        buttons_dropdown.click()
        sleep(5)
        if buttons_dropdown:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            for i in range(10):
                checkboxes = ['//input[contains(@id, "checkbox1")', '//input[contains(@id, "checkbox2")', '//input[contains(@id, "checkbox3")']
                selected = random.sample(checkboxes, 2)
                for checkbox_xpath in selected:
                    checkbox_element = self.driver.find_element(By.XPATH,checkbox_xpath + ']')  # Add ']' to complete the XPath
                    checkbox_element.click()
                    sleep(2)
                sleep(2)
                reset_button = self.driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-primary")]')
                reset_button.click()
                sleep(4)

    def test_random_Radio_buttons(self):
        buttons_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        buttons_dropdown.click()
        sleep(5)
        if buttons_dropdown:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            for i in range(10):
                checkboxes = ['//input[contains(@id, "checkbox1")]', '//input[contains(@id, "checkbox2")]', '//input[contains(@id, "checkbox3")]']
                selected = random.choice(checkboxes)
                self.driver.find_element(By.XPATH, selected).click()
                sleep(2)
                reset_button = self.driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-primary")]')
                reset_button.click()
                sleep(4)

if __name__ == "__main__":
    pytest.mark([__file__])