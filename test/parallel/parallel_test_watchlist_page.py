import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.watchlist_page import WatchlistPage
from logic.login_page import LoginPage
from infra.config_handler import ConfigHandler
import concurrent.futures
import time


class ParallelWatchlistTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config

    def run_watchlist_test_on_browser(self, browser_name):
        print(f"Running watchlist test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)
            login_page = LoginPage(driver)
            watchlist_page = WatchlistPage(driver)
            home_page.click_on_sign_in_link()
            login_page.enter_username_and_continue(self.config["user_name"])
            login_page.enter_password_and_login(self.config["password"])
            driver.get(self.config["url"])
            home_page.watchlist_click()
            watchlist_page.view_all_watched_items()
            time.sleep(10)
            assert "watchlist" in driver.current_url

        finally:
            driver.quit()

    def test_parallel_watchlist(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_watchlist_test_on_browser, browser): browser for browser in
                       self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Watchlist test completed on {browser}')


if __name__ == "__main__":
    unittest.main()
