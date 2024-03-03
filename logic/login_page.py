from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "userid")
    CONTINUE_BUTTON = (By.ID, "signin-continue-btn")
    PASSWORD_INPUT = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "sgnBt")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username_and_continue(self, username):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_input.send_keys(username)
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def enter_password_and_login(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.send_keys(password)
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        )
        sign_in_button.click()
