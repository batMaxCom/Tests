import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class YaDiskTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/list")
        self.assertIn("Авторизация", driver.title)
        button = driver.find_element(By.CLASS_NAME, "AuthLoginInputToggle-type")
        button.click()
        elem = driver.find_element("name", "login")
        elem.send_keys("my login")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elem_2 = driver.find_element("name", "passwd")
        elem_2.send_keys("my pawssword")
        elem_2.send_keys(Keys.RETURN)
        time.sleep(3)


    def tearDown(self):
        self.driver.close()