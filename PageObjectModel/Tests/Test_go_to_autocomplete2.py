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
        # self.driver = webdriver.Chrome("C:/Users/Maria/PycharmProjects/QA_Practice_Python/PageObjectModel/Resources"
        #                                "/chromedriver.exe")
        self.driver.get("http://formy-project.herokuapp.com/")

    def test_autocomplete(self):
        home = Home(self.driver)
        autocomplete = Autocomplete(self.driver)
        time.sleep(3)
        home.click_on_autocomplete()
        time.sleep(1)
        autocomplete.enter_adr("San Martin")
        time.sleep(2)
        autocomplete.enter_str1("George Enescu, 2")
        time.sleep(2)
        autocomplete.enter_str2("George Enescu, 3")
        time.sleep(2)
        autocomplete.enter_city("Bucuresti")
        time.sleep(2)
        autocomplete.enter_state("Romania")
        time.sleep(2)
        autocomplete.enter_zip("234567")
        time.sleep(2)
        autocomplete.enter_country("Romania")
        time.sleep(2)
        self.assertIn("San Martin", autocomplete.check_adr_result())

    def tearDown(self) -> None:
        self.driver.quit()
