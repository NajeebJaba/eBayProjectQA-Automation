import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.login_page import LoginPage
from logic.shopping_cart_with_login import ShoppingCartPage
from infra.config_handler import ConfigHandler
import concurrent.futures
import time

class ParallelShoppingCartTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config

    def run_shopping_cart_test_on_browser(self, browser_name):
        print(f"Running shopping cart test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()
        try:
            home_page = HomePage(driver)
            login_page = LoginPage(driver)
            cart_page = ShoppingCartPage(driver)
            home_page.click_on_sign_in_link()
            login_page.enter_username_and_continue(self.config["user_name"])
            login_page.enter_password_and_login(self.config["password"])
            driver.get(self.config["url"])
            home_page.click_cart_icon()
            cart_page.update_quantity_to_8()
            time.sleep(5)
            cart_page.remove_item()
            time.sleep(4)

        finally:
            driver.quit()

    def test_parallel_shopping_cart(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_shopping_cart_test_on_browser, browser): browser for browser in self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Shopping cart test completed on {browser}')

if __name__ == "__main__":
    unittest.main()

