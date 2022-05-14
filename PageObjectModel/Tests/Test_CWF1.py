import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.CompleteWebForm import CompleteWebForm
from PageObjectModel.Pages.Home import Home


class CompleteWF1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com")

    def test_CWF1(self):
        home = Home(self.driver)
        completed = CompleteWebForm(self.driver)
        time.sleep(2)
        home.click_on_CWF()
        time.sleep(2)
        completed.enter_first_name("George")
        time.sleep(2)
        completed.enter_last_name("Petrescu")
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()


