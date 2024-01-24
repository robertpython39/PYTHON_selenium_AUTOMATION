import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import random


@pytest.mark.functional
class TestButtonsDropdown:

    xpaths = ['//a[contains(@id,"date-picker")]',
              '//input[contains(@placeholder,"Pick a date")]'
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_data_pickers_button(self):
        try:
            data_pickers = self.driver.find_element(By.XPATH, self.xpaths[0])
            data_pickers.click()
            sleep(4)

            select_date = self.driver.find_element(By.XPATH, self.xpaths[1])
            sleep(2)
            random_month = random.randint(1, 12)
            random_day = random.randint(1, 29)
            random_year = random.randint(1990, 2500)
            select_date.send_keys(str(str(random_month) +'/' + str(random_day) + '/' + str(random_year)))
            sleep(3)

        except TimeoutError as ex:
            print("Exception has been thrown. " + str(ex))

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    pytest.mark([__file__])