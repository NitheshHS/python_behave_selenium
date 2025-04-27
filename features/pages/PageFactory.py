from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.product_page import ProductPage


class PageFactory(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page=None
        self.product_page=None

    def get_login_page(self):
        if self.login_page is None:
            self.login_page = LoginPage(self.driver)
        return self.login_page

    def get_product_page(self):
        if self.product_page is None:
            self.product_page = ProductPage(self.driver)
        return self.product_page