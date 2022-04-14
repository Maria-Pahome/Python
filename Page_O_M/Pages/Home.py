from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Base import Base


class Home(Base):
    AUTOCOMPLETE = (By.LINK_TEXT, "Autocomplete")
    BUTTONS = (By.LINK_TEXT, "Buttons")
    CHECKBOX = (By.LINK_TEXT, "Checkbox")
    DATE = (By.LINK_TEXT, "Datepicker")
    DRAG = (By.LINK_TEXT, "Drag and Drop")
    DROPDOWN = (By.LINK_TEXT, "Dropdown")
    ENABLE = (By.LINK_TEXT, "Enable and disable elements ")
    FILEUPLOAD = (By.LINK_TEXT, "File Upload")
    KEY_MOUSE = (By.LINK_TEXT, "Key and Mouse Press")
    MODAL = (By.LINK_TEXT, "Modal")
    PAGE_SCROLL = (By.LINK_TEXT, "Page Scroll")
    RADIOBUTTON = (By.LINK_TEXT, "Radio Button")
    SWITCH = (By.LINK_TEXT, "Switch Window")
    COMPLETE = (By.LINK_TEXT, "Complete Web Form")

    def click_on_autocomplete(self):
        self._driver.find_element(*self.AUTOCOMPLETE).click()
        print("We'll go to autocomplete page.")

    def click_on_checkbox(self):
        self._driver.find_element(*self.CHECKBOX).click()
        print("We'll go to checkbox page.")

    def click_on_buttons(self):
        self._driver.find_element(*self.BUTTONS).click()
        print("We'll go to buttons page.")

