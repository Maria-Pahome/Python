from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class Autocomplete(Base):
    ADDRESS = (By.ID, "autocomplete")
    STR1 = (By.ID, "street_number")
    STR2 = (By.ID, "route")
    CITY = (By.ID, "locality")
    STATE = (By.ID, "administrative_area_level_1")
    ZIPCODE = (By.ID, "postal_code")
    COUNTRY = (By.ID, "country")

    def enter_adr(self, address):
        self._driver.find_element(*self.ADDRESS).click()
        self._driver.find_element(*self.ADDRESS).send_keys(address)
        print("The following address was entered " + address)

    def enter_str1(self, street1):
        self._driver.find_element(*self.STR1).click()
        self._driver.find_element(*self.STR1).send_keys(street1)
        print("The following address was entered " + street1)

    def enter_str2(self, street2):
        self._driver.find_element(*self.STR2).click()
        self._driver.find_element(*self.STR2).send_keys(street2)
        print("The following address was entered " + street2)

    def enter_city(self, city):
        self._driver.find_element(*self.CITY).click()
        # self._driver.find_element(*self.CITY).send_keys(city)
        print("The following address was entered " + city)

    def enter_state(self, state):
        self._driver.find_element(*self.STATE).click()
        self._driver.find_element(*self.STATE).send_keys(state)
        print("The following address was entered " + state)

    def enter_zip(self, zipcode):
        self._driver.find_element(*self.ZIPCODE).click()
        self._driver.find_element(*self.ZIPCODE).send_keys(zipcode)
        print("The following address was entered " + zipcode)

    def enter_country(self, country):
        self._driver.find_element(*self.COUNTRY).click()
        self._driver.find_element(*self.COUNTRY).send_keys(country)
        print("The following address was entered " + country)

    def check_adr_result(self):
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "body > div.pac-container.hdpi > div > div:nth-child(2) > span").text
