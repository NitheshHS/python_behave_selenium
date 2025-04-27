from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._user_name = (By.ID, 'user-name')
        self._password = (By.ID, 'password')
        self._login_button = (By.ID, 'login-button')

    def enter_username(self, username):
        self.driver.find_element(*self._user_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self._password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self._login_button).click()