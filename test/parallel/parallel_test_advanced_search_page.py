import unittest
import concurrent.futures
import time
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.login_page import LoginPage
from logic.advanced_search_page import AdvancedSearchPage
from infra.config_handler import ConfigHandler


class ParallelAdvancedSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.item_id = cls.config["item_id"]

    def run_advanced_search_test_on_browser(self, browser_name):
        print(f"Running advanced search test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)
            login_page = LoginPage(driver)
            advanced_search_page = AdvancedSearchPage(driver)

            home_page.click_on_sign_in_link()
            login_page.enter_username_and_continue(self.config["user_name"])
            login_page.enter_password_and_login(self.config["password"])
            time.sleep(2)

            driver.get(f"{self.config['url']}sch/ebayadvsearch")

            advanced_search_page.enter_item_id_and_search(self.item_id)
            time.sleep(2)
            advanced_search_page.select_first_result_and_add_to_watchlist()
            time.sleep(3)

        finally:
            driver.quit()

    def test_parallel_advanced_search(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_advanced_search_test_on_browser, browser): browser for browser in
                       self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Advanced search test completed on {browser}')


if __name__ == "__main__":
    unittest.main()
