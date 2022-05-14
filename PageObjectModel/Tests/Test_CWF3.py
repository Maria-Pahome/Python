import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.CompleteWebForm import CompleteWebForm


class CompleteWF3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/form")

    def test_CWF3(self):
        completed = CompleteWebForm(self.driver)
        time.sleep(2)
        completed.level_ed1()
        time.sleep(1)
        completed.level_ed2()
        time.sleep(1)
        completed.level_ed3()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()

