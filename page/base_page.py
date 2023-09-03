class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, args):
        return self.driver.find_element(*args)

    def finds(self, args):
        return self.driver.find_elements(*args)
