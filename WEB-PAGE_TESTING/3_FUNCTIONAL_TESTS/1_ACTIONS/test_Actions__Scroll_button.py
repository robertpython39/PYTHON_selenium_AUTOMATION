import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.functional
class TestClickActionsMenu:

    xpaths = [
        '//a[contains(@id,"actions")]',
        '//a[contains(@id,"scroll")]'
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
        sleep(4)  # Adjust the sleep duration based on page load time

        scroll_button = self.driver.find_element(By.XPATH, self.xpaths[1])
        scroll_button.click()
        sleep(2)  # Sleep to allow the page to fully load

        for position in range (250, 1050, 50):
            self.driver.execute_script(f"window.scrollBy(0, {position});")
            sleep(0.5)

if __name__ == "__main__":
    pytest.main([__file__])
