import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.CompleteWebForm import CompleteWebForm
from PageObjectModel.Pages.Home import Home


class CompleteWF2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com")
        time.sleep(2)
        self.driver.maximize_window()

    def test_CWF2(self):
        home = Home(self.driver)
        completed = CompleteWebForm(self.driver)
        time.sleep(2)
        home.click_on_CWF()
        time.sleep(2)
        completed.enter_first_name("Tatiana")
        time.sleep(2)
        completed.enter_last_name("Popescu")
        time.sleep(2)
        completed.job_title("teacher")
        time.sleep(2)
        self.driver.back()
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.quit()
