import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CompleteWF4(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")

    def test_CWF4(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "radio-button-1").click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, "radio-button-1").click()
        self.assertIsNotNone(result, "This is a bug!")

    def tearDown(self) -> None:
        self.driver.quit()
