from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class CompleteWebForm(Base):
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, "job-title")
    LEVEL = (By.LINK_TEXT, "Highest level of education")
    GENDER = (By.CSS_SELECTOR, "body > div > form > div > div:nth-child(9) > div:nth-child(1) > strong > label")
    EXPERIENCE = (By.ID, "select-menu")
    DATE = (By.ID, "datepicker")
    SUBMIT = (By.CSS_SELECTOR, "body > div > form > div > div:nth-child(15) > a")

    def enter_first_name(self, first_name):
        self._driver.find_element(*self.FIRSTNAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self._driver.find_element(*self.LASTNAME).send_keys(last_name)

    def job_title(self, job_title):
        self._driver.find_element(*self.JOB_TITLE).send.keys(job_title)

    def level_education(self):
        self._driver.find_element(*self.LEVEL).click()

    def gender(self):
        self._driver.find_element(*self.GENDER).click()

    def experience(self):
        self._driver.find_element(*self.EXPERIENCE).click()

    def pick_date(self):
        self._driver.find_element(*self.DATE).click()

    def submit(self):
        self._driver.find_element(*self.SUBMIT).click()
