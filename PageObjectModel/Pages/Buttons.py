from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class Buttons(Base):
    PRIMARY_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > div > button.btn.btn-lg.btn-primary")
    SUCCESS_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > div > button.btn.btn-lg.btn-success")
    INFO_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > div > button.btn.btn-lg.btn-info")
    WARNING_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > div > button.btn.btn-lg.btn-warning")
    DANGER_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > div > button.btn.btn-lg.btn-danger")
    LINK_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > div > div > button.btn.btn-lg.btn-link")
    LEFT_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(2) > div > div > div > button:nth-child(1)")
    MIDDLE_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(2) > div > div > div > button:nth-child(2)")
    RIGHT_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(2) > div > div > div > button:nth-child(3)")
    ONE_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(3) > div > div > div > button:nth-child(1)")
    TWO_BTN = (By.CSS_SELECTOR, "body > div > form > div:nth-child(3) > div > div > div > button:nth-child(2)")
    DROPDOWN_BTN = (By.ID, "btnGroupDrop1")
    DROPDOWN_BTN1 = (
    By.CSS_SELECTOR, "body > div > form > div:nth-child(3) > div > div > div > div > div > a:nth-child(1)")

    def primary(self):
        self._driver.find_element(*self.PRIMARY_BTN).click()

    def success(self):
        self._driver.find_element(*self.SUCCESS_BTN).click()

    def info(self):
        self._driver.find_element(*self.INFO_BTN).click()

    def warning(self):
        self._driver.find_element(*self.WARNING_BTN).click()

    def danger(self):
        self._driver.find_element(*self.DANGER_BTN).click()

    def link(self):
        self._driver.find_element(*self.LINK_BTN).click()

    def left(self):
        self._driver.find_element(*self.LEFT_BTN).click()

    def middle(self):
        self._driver.find_element(*self.MIDDLE_BTN).click()

    def right(self):
        self._driver.find_element(*self.RIGHT_BTN).click()

    def button_one(self):
        self._driver.find_element(*self.ONE_BTN).click()

    def button_two(self):
        self._driver.find_element(*self.TWO_BTN).click()

    def dropdown(self):
        self._driver.find_element(*self.DROPDOWN_BTN).click()

    def dropdown_1(self):
        self._driver.find_element(*self.DROPDOWN_BTN1).click()


