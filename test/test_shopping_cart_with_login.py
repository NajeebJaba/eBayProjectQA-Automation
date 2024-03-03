import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.login_page import LoginPage
from logic.shopping_cart_with_login import ShoppingCartPage
from infra.config_handler import ConfigHandler


class TestShoppingCartWithLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()

    def setUp(self):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.cart_page = ShoppingCartPage(self.driver)

    def test_shopping_cart_actions(self):
        self.home_page.click_on_sign_in_link()
        self.login_page.enter_username_and_continue(self.config["user_name"])
        self.login_page.enter_password_and_login(self.config["password"])
        self.driver.get(self.config["url"])
        self.home_page.click_cart_icon()
        self.cart_page.update_quantity_to_8()
        time.sleep(5)
        self.cart_page.remove_item()
        time.sleep(4)

    def tearDown(self):
        self


if __name__ == "__main__":
    unittest.main()
