import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.functional
class TestNewTabWindowDropdown:

    xpaths = ['//a[text()="New Tab / Window"]',
              '//a[text()="New Browser Tab"]',
              '//a[text()="New Browser Window"]'
    ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_new_browser_tab(self):
        new_browser = self.driver.find_element(By.XPATH, self.xpaths[0])
        new_browser.click()
        sleep(3)
        if new_browser:
            new_browserTab = self.driver.find_element(By.XPATH, self.xpaths[1])
            new_browserTab.click()
            sleep(3)

    def test_new_browser_window(self):
        new_browser = self.driver.find_element(By.XPATH, self.xpaths[0])
        new_browser.click()
        sleep(3)
        if new_browser:
            new_browserTab = self.driver.find_element(By.XPATH, self.xpaths[2])
            new_browserTab.click()
            sleep(3)

        self.driver.minimize_window()
        self.driver.quit()

if __name__ == "__main__":
    pytest.mark([__file__])

