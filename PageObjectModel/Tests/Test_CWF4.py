import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.CompleteWebForm import CompleteWebForm


class CompleteWF4(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")

    def test_CWF4(self):
        completed = CompleteWebForm(self.driver)
        completed.level_ed1()
        time.sleep(2)
        result = completed.level_ed1()
        self.assertIsNotNone(result, "This is a bug!")

    def tearDown(self) -> None:
        self.driver.quit()

