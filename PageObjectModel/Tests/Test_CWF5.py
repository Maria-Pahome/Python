
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CompleteWF5(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")

    def gender_check(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "checkbox-1").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "checkbox-2").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "checkbox-3").click()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()