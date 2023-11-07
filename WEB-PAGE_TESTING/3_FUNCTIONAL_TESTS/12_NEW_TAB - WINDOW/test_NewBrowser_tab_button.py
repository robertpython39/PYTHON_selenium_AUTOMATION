import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.functional
class TestNewBrowserTab:
    xpaths = ['//a[text()="New Tab / Window"]',
              '//a[text()="New Browser Tab"]',
              '//a[text()="Press me - New Tab"]',
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_new_browser_tab(self):
        newTab = self.driver.find_element(By.XPATH, self.xpaths[0])
        newTab.click()
        if newTab:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
            self.driver.find_element(By.XPATH, self.xpaths[2]).click()
            sleep(4)
        self.driver.quit()

if __name__ == "__main__":
    pytest.mark([__file__, "-v"])
