import unittest
import time
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.watchlist_page import WatchlistPage
from logic.login_page import LoginPage
from infra.config_handler import ConfigHandler


class TestWatchlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.initialize_driver()

    def test_view_watchlist(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        watchlist_page = WatchlistPage(self.driver)
        home_page.click_on_sign_in_link()
        login_page.enter_username_and_continue(self.config["user_name"])
        login_page.enter_password_and_login(self.config["password"])
        self.driver.get(self.config["url"])
        home_page.watchlist_click()
        watchlist_page.view_all_watched_items()
        time.sleep(10)  # stay on the watchlist page to view items, to explain about the test
        self.assertIn("watchlist", self.driver.current_url, "Not on the watchlist page.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
