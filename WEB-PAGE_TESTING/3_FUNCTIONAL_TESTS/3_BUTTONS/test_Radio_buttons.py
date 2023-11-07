import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.functional
class TestButtonsDropdown:

    xpaths = ['//a[text()="Buttons"]',
              '//a[text()="Radio buttons"]'
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_Radio_buttons(self):
        buttons_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        buttons_dropdown.click()
        sleep(5)
        if buttons_dropdown:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            for i in range(22):
                radio_buttons=['//input[contains(@id, "radio-button1")]', '//input[contains(@id, "radio-button2")]', '//input[contains(@id, "radio-button3")]']
                selected = random.choice(radio_buttons)
                self.driver.find_element(By.XPATH, selected).click()
                sleep(2)

if __name__ == "__main__":
    pytest.mark([__file__])

