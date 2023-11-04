import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@pytest.mark.functional
class TestClickActionsMenu:

    xpaths = [
        '//a[contains(@id,"actions")]',
        '//a[contains(@id,"double-click")]',
        '//button[contains(@class,"btn btn-primary")]'
    ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_double_click_button(self):
        actions_button = self.driver.find_element(By.XPATH, self.xpaths[0])
        if actions_button:
            actions_button.click()
            sleep(5)
            double_click_button = self.driver.find_element(By.XPATH, self.xpaths[1])
            double_click_button.click()
            sleep(5)
            perform_click = self.driver.find_element(By.XPATH, self.xpaths[2])
            if perform_click:
                action_chains = ActionChains(self.driver)
                action_chains.double_click(perform_click).perform()
                sleep(5)

if __name__ == "__main__":
    pytest.main([__file__])
