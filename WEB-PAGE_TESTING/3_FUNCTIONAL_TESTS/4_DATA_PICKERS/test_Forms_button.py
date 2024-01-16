import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.functional
class TestButtonsDropdown:

    #TODO: Implement xpaths
    xpaths = [
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    #TODO: Implement steps
    def test_(self):
        pass




if __name__ == "__main__":
    pytest.mark([__file__])