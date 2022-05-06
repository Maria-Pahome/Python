import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CompleteWF2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")
        time.sleep(2)

    def test_CWF2(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "first-name").send_keys("Tatiana")
        time.sleep(1)
        self.driver.find_element(By.ID, "last-name").send_keys("Popescu")
        time.sleep(1)
        self.driver.find_element(By.ID, "job-title").send_keys("teacher")
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()
