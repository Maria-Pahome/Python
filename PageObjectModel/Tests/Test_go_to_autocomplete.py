import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GoToAutocomplete(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome("C:/Users/Maria/PycharmProjects/QA_Practice_Python/PageObjectModel/Resources"
        #                                "/chromedriver.exe")
        self.driver.get("http://formy-project.herokuapp.com/")

    def test_autocomplete(self):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Autocomplete").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "autocomplete").send_keys("Bucharest")
        time.sleep(1)
        self.driver.find_element(By.ID, "street_number").send_keys("Anton Pan, 20")
        time.sleep(1)
        self.driver.find_element(By.ID, "route").send_keys("Anton Pan, 15")
        time.sleep(1)
        self.driver.find_element(By.ID, "locality").send_keys("Washington")
        time.sleep(1)
        self.driver.find_element(By.ID, "administrative_area_level_1").send_keys("Romania")
        time.sleep(1)
        self.driver.find_element(By.ID, "postal_code").send_keys("344567")
        time.sleep(1)
        self.driver.find_element(By.ID, "country").send_keys("Romania")
        time.sleep(1)
        result = self.driver.find_element(By.CSS_SELECTOR,
                                          "body > div.pac-container.hdpi > div > div:nth-child(2) > span")
        self.assertIn("Bucharest", result.text)

    def tearDown(self) -> None:
        self.driver.quit()
