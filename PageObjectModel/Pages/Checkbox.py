from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class Checkbox(Base):
    CHECK1 = (By.ID, "checkbox-1")
    CHECK2 = (By.ID, "checkbox-2")
    CHECK3 = (By.ID, "checkbox-3")

    def checkbox_1(self):
        self._driver.find_element(*self.CHECK1).click()

    def checkbox_2(self):
        self._driver.find_element(*self.CHECK2).click()

    def checkbox_3(self):
        self._driver.find_element(*self.CHECK3).click()
