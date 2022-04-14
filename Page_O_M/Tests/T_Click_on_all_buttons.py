import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Buttons import Buttons


def click_on_all_buttons():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://formy-project.herokuapp.com/buttons")
    driver.maximize_window()
    time.sleep(2)
    all_buttons = Buttons(driver)
    all_buttons.primary()
    time.sleep(2)
    all_buttons.success()
    time.sleep(2)
    all_buttons.info()
    time.sleep(2)
    all_buttons.warning()
    time.sleep(2)
    all_buttons.danger()
    time.sleep(2)
    all_buttons.link()
    time.sleep(2)
    all_buttons.left()
    time.sleep(2)
    all_buttons.middle()
    time.sleep(2)
    all_buttons.right()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    click_on_all_buttons()
