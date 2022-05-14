
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.CompleteWebForm import CompleteWebForm
from PageObjectModel.Pages.Home import Home


class CompleteWF5(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com")

    def gender_check(self):
        home = Home(self.driver)
        completed = CompleteWebForm(self.driver)
        time.sleep(2)
        home.click_on_CWF()
        time.sleep(2)
        completed.gender1()
        time.sleep(2)
        completed.gender2()
        time.sleep(2)
        completed.gender3()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()
