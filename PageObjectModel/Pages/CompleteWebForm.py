from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class CompleteWebForm(Base):
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, "job-title")
    LEVEL_ED1 = (By.ID, "radio-button-1")
    LEVEL_ED2 = (By.ID, "radio-button-2")
    LEVEL_ED3 = (By.ID, "radio-button-3")
    GENDER1 = (By.ID, "checkbox-1")
    GENDER2 = (By.ID, "checkbox-2")
    GENDER3 = (By.ID, "checkbox-3")
    EXPERIENCE = (By.ID, "select-menu")
    DATE = (By.ID, "datepicker")
    SUBMIT = (By.CSS_SELECTOR, "body > div > form > div > div:nth-child(15) > a")

    def enter_first_name(self, first_name):
        self._driver.find_element(*self.FIRSTNAME).click()
        self._driver.find_element(*self.FIRSTNAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self._driver.find_element(*self.LASTNAME).click()
        self._driver.find_element(*self.LASTNAME).send_keys(last_name)

    def job_title(self, job_title):
        self._driver.find_element(*self.JOB_TITLE).click()
        self._driver.find_element(*self.JOB_TITLE).send_keys(job_title)

    def level_ed1(self):
        self._driver.find_element(*self.LEVEL_ED1).click()

    def level_ed2(self):
        self._driver.find_element(*self.LEVEL_ED2).click()

    def level_ed3(self):
        self._driver.find_element(*self.LEVEL_ED3).click()

    def gender1(self):
        self._driver.find_element(*self.GENDER1).click()

    def gender2(self):
        self._driver.find_element(*self.GENDER2).click()

    def gender3(self):
        self._driver.find_element(*self.GENDER3).click()

    def experience(self):
        self._driver.find_element(*self.EXPERIENCE).click()

    def pick_date(self):
        self._driver.find_element(*self.DATE).click()

    def submit(self):
        self._driver.find_element(*self.SUBMIT).click()
