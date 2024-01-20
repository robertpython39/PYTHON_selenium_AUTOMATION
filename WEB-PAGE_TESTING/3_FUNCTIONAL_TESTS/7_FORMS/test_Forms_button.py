import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep


@pytest.mark.functional
class TestButtonsDropdown:

    xpaths = ['//a[contains(@href, "#homeSubmenu")]',
              '//a[contains(@id, "login")]',
              '//a[contains(@id, "register")]',
              '//a[contains(@id, "recover-password")]'
              ]

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()
        forms_dropdown = self.driver.find_element(By.XPATH, self.xpaths[0])
        forms_dropdown.click()
        sleep(3)


    def teardown_method(self):
        self.driver.quit()


    def test_1_Login(self):
        try:
            login_button = self.driver.find_element(By.XPATH, self.xpaths[1])
            login_button.click()
            sleep(3)

            input_email = self.driver.find_element(By.XPATH, '//input[contains(@type, "email")]')
            input_email.send_keys("admin@admin.com")
            sleep(3)

            input_password = self.driver.find_element(By.XPATH, '//input[contains(@type, "password")]')
            input_password.send_keys("admin123")
            sleep(3)

            submit_bttn = self.driver.find_element(By.XPATH, '//button[contains(@id, "submitLoginBtn")]')
            submit_bttn.click()
            sleep(3)


        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        except TimeoutException as e:
            print(f"Timeout waiting for element: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def test_2_Register(self):

        register_Button = self.driver.find_element(By.XPATH, self.xpaths[2])
        register_Button.click()
        sleep(3)
        try:
            input_firstN = self.driver.find_element(By.XPATH,'//input[contains(@id,"firstName")]')
            input_firstN.send_keys("test1234")
            sleep(3)

            input_lastN = self.driver.find_element(By.XPATH,'//input[contains(@id,"lastName")]')
            input_lastN.send_keys("test2345")
            sleep(3)

            input_phone = self.driver.find_element(By.XPATH,'//input[contains(@id,"phone")]')
            input_phone.send_keys('0725383561')
            sleep(3)

            input_country = self.driver.find_element(By.XPATH, '//select[contains(@id,"countries")]')
            input_country.click()
            dropdowns = Select(input_country)
            dropdowns.select_by_visible_text('Argentina')

            input_email = self.driver.find_element(By.XPATH,'//input[contains(@id,"emailAddress")]')
            input_email.send_keys('test1234@test.com')
            sleep(3)

            input_password = self.driver.find_element(By.XPATH,'//input[contains(@id,"password")]')
            input_password.send_keys('test11111')
            sleep(3)

            input_agreeCheck = self.driver.find_element(By.XPATH,'//input[contains(@id,"exampleCheck1")]')
            input_agreeCheck.click()
            sleep(3)

            bttn_register = self.driver.find_element(By.XPATH, '//button[contains(@onclick,"registerAccount()")]')
            bttn_register.click()
            sleep(3)


        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        except TimeoutException as e:
            print(f"Timeout waiting for element: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def test_3_Recover_password(self):
        try:
            recover_button = self.driver.find_element(By.XPATH, self.xpaths[3])
            recover_button.click()
            recover_bttn = self.driver.find_element(By.XPATH, '//button[contains(@id,"recover-password")]')
            recover_input = self.driver.find_element(By.XPATH, '//input[contains(@id,"email")]')
            recover_input.send_keys('test1234@test.com')
            sleep(3)
            recover_bttn.click()
            sleep(3)

        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        except TimeoutException as e:
            print(f"Timeout waiting for element: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    pytest.mark([__file__])