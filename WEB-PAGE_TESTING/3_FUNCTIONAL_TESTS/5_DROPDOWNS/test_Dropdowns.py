import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


@pytest.mark.functional
class TestButtonsDropdown:

    xpaths = ['//a[contains(@href,"dropdowns")]',
              '//select[contains(@id,"dropdown-menu")]'
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()
        dropdown_button = self.driver.find_element(By.XPATH, self.xpaths[0])
        dropdown_button.click()


    def teardown_method(self):
        self.driver.quit()

    def test_country_selection(self):
        try:
            simple_dropdown = self.driver.find_element(By.XPATH, self.xpaths[1])
            simple_dropdown.click()
            sleep(5)
            country_select = Select(simple_dropdown)
            country_select.select_by_visible_text("Argentina")
            sleep(5)

        except TimeoutError as ex:
            print("Exception has been thrown. " + str(ex))

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def test_hover_dropdown_someAction(self):
        try:
            dropdown_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"multi-level")]')
            dropdown_button.click()
            sleep(5)
            some_action = self.driver.find_element(By.XPATH, '//a[contains(@href,"#some-action")]')
            some_action.click()
            sleep(5)

        except TimeoutError as ex:
            print("Exception has been thrown. " + str(ex))

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def test_hover_otherAction(self):
        try:
            dropdown_button = self.driver.find_element(By.XPATH, '//button[contains(@id,"multi-level")]')
            dropdown_button.click()
            sleep(5)

            other_action = self.driver.find_element(By.XPATH, '//li[contains(@class,"dropdown-item")]//.//a[contains(@href,"#some-other")]')
            other_action.click()
            sleep(4)

        except TimeoutError as ex:
            print("Exception has been thrown. " + str(ex))

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    pytest.mark([__file__])