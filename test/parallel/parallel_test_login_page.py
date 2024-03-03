import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.login_page import LoginPage
from infra.config_handler import ConfigHandler
import concurrent.futures
import time


class GridTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.HUB_URL = cls.config["hub_url"]
        cls.browsers = cls.config["browser_types"]

    def setUp(self):
        pass

    def run_test_on_browser(self, browser_name):
        print(f"Running test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            driver.get(self.config["url"])
            home_page = HomePage(driver)
            home_page.click_on_sign_in_link()

            login_page = LoginPage(driver)
            login_page.enter_username_and_continue(self.config["user_name"])
            time.sleep(2)
            login_page.enter_password_and_login(self.config["password"])
            time.sleep(10)
            driver.get(self.config["url"])
            time.sleep(5)
            return driver.title
        finally:
            driver.quit()

    def test_login(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_test_on_browser, browser): browser for browser in self.browsers}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'{browser} page title after login is: {result}')


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
