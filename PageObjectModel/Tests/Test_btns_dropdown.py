import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Buttons import Buttons
from PageObjectModel.Pages.Home import Home


def btns_dropdown():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://formy-project.herokuapp.com/")
    driver.maximize_window()
    time.sleep(2)
    home = Home(driver)
    dropdown_btn = Buttons(driver)
    home.click_on_buttons()
    time.sleep(2)
    dropdown_btn.dropdown()
    time.sleep(2)
    dropdown_btn.dropdown_1()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    btns_dropdown()
