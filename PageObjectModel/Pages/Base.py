class Base:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(10)
