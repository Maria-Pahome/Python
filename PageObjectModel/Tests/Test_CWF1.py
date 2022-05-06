import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CompleteWF1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")

    def test_CWF1(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "first-name").send_keys("George")
        time.sleep(2)
        self.driver.find_element(By.ID, "last-name").send_keys("Petrescu")
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()
