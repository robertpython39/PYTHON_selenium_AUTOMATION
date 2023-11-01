# imports
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.functional
class TestClickActionsMenu:

    xpaths=['//a[text()="Actions"]',
            '//a[contains(@id,"double-click")]',
            '//a[contains(@id,"scroll")]',
            '//a[contains(@id,"mouse-hover")]',
            '//a[contains(@id,"show-hide-element")]'
            ]


    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url="https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()



    def test_double_click_button(self, setup_teardown):
        try:
            self.driver.find_element(By.XPATH, self.xpaths[1]).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n{e}")

    def test_scrolling_button(self, setup_teardown):
        try:
            self.driver.find_element(By.XPATH, self.xpaths[2]).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n{e}")


    def test_mouse_hover_button(self, setup_teardown):
        try:
            self.driver.find_element(By.XPATH, self.xpaths[3]).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n{e}")


    def test_show_hide_button(self, setup_teardown):
        try:
            self.driver.find_element(By.XPATH, self.xpaths[4]).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n{e}")

class Test_Double_click_button():
    pass

class Test_Scrolling_button():
    pass

class Test_Mouse_hover_button():
    pass

class Test_Show_hide_element():
    pass
