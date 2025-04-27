from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self._product_names=(By.XPATH, "//div[@class='inventory_item_name']")

    def get_all_products(self):
       return self.driver.find_elements(*self._product_names)

