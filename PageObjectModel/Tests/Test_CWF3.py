import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CompleteWF3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")

    def test_CWF3(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "radio-button-1").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "radio-button-2").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "radio-button-3").click()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()
