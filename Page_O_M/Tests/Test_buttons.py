import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Buttons import Buttons
from PageObjectModel.Pages.Home import Home


def test_buttons():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://formy-project.herokuapp.com/")
    driver.maximize_window()
    time.sleep(4)
    home = Home(driver)
    buttons = Buttons(driver)
    home.click_on_buttons()
    time.sleep(4)
    buttons.primary()
    time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    test_buttons()
