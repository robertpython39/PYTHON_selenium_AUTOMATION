import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@pytest.mark.functional
class TestClickActionsMenu:

    xpaths = [
        '//a[contains(@id,"actions")]',
        '//a[contains(@id,"show-hide-element")]',
        '//button[contains(@class,"btn btn-info")]'
    ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_ShowHide_element(self):
        actions_button = self.driver.find_element(By.XPATH, self.xpaths[0])
        actions_button.click()
        sleep(6)
        if actions_button:
            show_hide_elem = self.driver.find_element(By.XPATH, self.xpaths[1])
            show_hide_elem.click()
            sleep(5)
            button_click = self.driver.find_element(By.XPATH, self.xpaths[2])
            button_click.click()
            sleep(5)
            button_click.click()
            sleep(5)
            self.driver.minimize_window()


if __name__ == "__main__":
    pytest.main[(__file__)]