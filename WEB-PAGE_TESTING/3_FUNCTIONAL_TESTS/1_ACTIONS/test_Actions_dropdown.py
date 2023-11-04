import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.functional
class TestClickActionsMenu:

    xpaths = [
        '//a[contains(@id,"actions")]',
        '//a[contains(@id,"double-click")]',
        '//a[contains(@id,"scroll")]',
        '//a[contains(@id,"mouse-hover")]',
        '//a[contains(@id,"show-hide-element")]'
    ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_Actions_button(self):
        actions_button = self.driver.find_element(By.XPATH, self.xpaths[0])
        if actions_button:
            actions_button.click()
            sleep(5)
            return actions_button
        else:
            return None

    def test_double_click(self):
        actions_button = self.test_Actions_button()
        if actions_button:
            double_click = self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(7)

    def test_scroll_button(self):
        actions_button = self.test_Actions_button()
        if actions_button:
            scroll = self.driver.find_element(By.XPATH, self.xpaths[2]).click()
            sleep(7)

    def test_hover_button(self):
        actions_button = self.test_Actions_button()
        if actions_button:
            hover = self.driver.find_element(By.XPATH, self.xpaths[3]).click()
            sleep(7)

    def test_show_hide_button(self):
        actions_button = self.test_Actions_button()
        if actions_button:
            show_hide = self.driver.find_element(By.XPATH, self.xpaths[4]).click()
            sleep(7)

if __name__ == "__main__":
    pytest.main([__file__])
