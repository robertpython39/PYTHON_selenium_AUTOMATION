import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.functional
class TestButtonsDropdown:

    xpaths = ['//a[text()="Buttons"]',
              '//a[text()="Checkboxes"]',
              '//a[text()="Radio buttons"]'
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_click_Buttons_button(self):
        ButtonsButton = self.driver.find_element(By.XPATH, self.xpaths[0])
        return ButtonsButton

    def test_click_Checkboxes_button(self):
        self.test_click_Buttons_button().click()
        checkboxes = self.driver.find_element(By.XPATH, self.xpaths[1])
        checkboxes.click()
        sleep(5)

    def test_Radio_buttons(self):
        self.test_click_Buttons_button().click()
        radioButtons = self.driver.find_element(By.XPATH, self.xpaths[2])
        radioButtons.click()
        sleep(5)

if __name__ == "__main__":
    pytest.mark([__file__])