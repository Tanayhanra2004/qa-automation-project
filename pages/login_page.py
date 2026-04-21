from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def login(self, username, password):
        self.find(self.username).send_keys(username)
        self.find(self.password).send_keys(password)
        self.find(self.login_btn).click()