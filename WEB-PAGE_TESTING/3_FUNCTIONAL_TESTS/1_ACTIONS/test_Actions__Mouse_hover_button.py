import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@pytest.mark.functional
class TestClickActionsMenu:

    xpaths = [
        '//a[contains(@id,"actions")]',
        '//a[contains(@id,"mouse-hover")]',
        '//button[contains(@id,"button-hover-over")]'
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
            mouse_hover = self.driver.find_element(By.XPATH, self.xpaths[1])
            mouse_hover.click()
            hover = self.driver.find_element(By.XPATH, self.xpaths[2])
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(hover).perform()
            sleep(5)
            hover.click()

if __name__ == "__main__":
    pytest.mark([__file__])