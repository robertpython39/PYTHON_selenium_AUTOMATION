# imports
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestAllButtons():

    xpaths = []
    with open("xpaths.txt") as xph:
        for line in xph:
            xpaths.append(line)


    # def __init__(self, url):
    #     self.driver = webdriver.Chrome()
    #     self.url = url
    #     self.driver.get(url=self.url)
    #     self.driver.maximize_window()
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-automation-practice.netlify.app/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_button_1(self):
        try:
            xpath1 = self.xpaths[0]
            self.driver.find_element(By.XPATH, xpath1).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_2(self):
        try:
            xpath2 = self.xpaths[1]
            self.driver.find_element(By.XPATH, xpath2).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_3(self):
        try:
            xpath3 = self.xpaths[2]
            self.driver.find_element(By.XPATH, xpath3).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_4(self):
        try:
            xpath4 = self.xpaths[3]
            self.driver.find_element(By.XPATH, xpath4).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_5(self):
        try:
            xpath5 = self.xpaths[4]
            self.driver.find_element(By.XPATH, xpath5).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_6(self):
        try:
            xpath6 = self.xpaths[5]
            self.driver.find_element(By.XPATH, xpath6).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_7(self):
        try:
            xpath7 = self.xpaths[6]
            self.driver.find_element(By.XPATH, xpath7).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_8(self):
        try:
            xpath8 = self.xpaths[7]
            self.driver.find_element(By.XPATH, xpath8).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_9(self):
        try:
            xpath9 = self.xpaths[8]
            self.driver.find_element(By.XPATH, xpath9).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_10(self):
        try:
            xpath10 = self.xpaths[9]
            self.driver.find_element(By.XPATH, xpath10).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_11(self):
        try:
            xpath11 = self.xpaths[10]
            self.driver.find_element(By.XPATH, xpath11).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_12(self):
        try:
            xpath12 = self.xpaths[11]
            self.driver.find_element(By.XPATH, xpath12).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_13(self):
        try:
            xpath13 = self.xpaths[12]
            self.driver.find_element(By.XPATH, xpath13).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_14(self):
        try:
            xpath14 = self.xpaths[13]
            self.driver.find_element(By.XPATH, xpath14).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_15(self):
        try:
            xpath15 = self.xpaths[14]
            self.driver.find_element(By.XPATH, xpath15).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")

    def test_button_16(self):
        try:
            xpath16 = self.xpaths[15]
            self.driver.find_element(By.XPATH, xpath16).click()
            sleep(5)
        except Exception as e:
            print(f"Error code:\n {e}")
