import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Buttons import Buttons
from PageObjectModel.Pages.Home import Home


def btns_displayed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://formy-project.herokuapp.com/buttons#")
    driver.maximize_window()
    time.sleep(4)
    bottom_btns = Buttons(driver)
    time.sleep(2)
    bottom_btns.button_one()
    time.sleep(2)
    bottom_btns.button_two()
    time.sleep(2)
    bottom_btns.dropdown()
    time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    btns_displayed()
