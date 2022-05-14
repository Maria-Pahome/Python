import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Autocomplete import Autocomplete
from PageObjectModel.Pages.Home import Home


class GoToAutocomplete2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://formy-project.herokuapp.com/")

    def test_autocomplete(self):
        home = Home(self.driver)
        autocomplete = Autocomplete(self.driver)
        time.sleep(3)
        home.click_on_autocomplete()
        time.sleep(1)
        autocomplete.enter_adr("San Martin")
        time.sleep(2)
        self.assertIn("San Martin", autocomplete.check_adr_result())

    def tearDown(self) -> None:
        self.driver.quit()

