import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.filter_item_page import FilterItemPage
from infra.config_handler import ConfigHandler

class TestFilterItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config

    def test_filter_item(self):
        browser_wrapper = BrowserWrapper()
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)
            home_page.search_for_item(self.config["search_item"])
            filter_page = FilterItemPage(driver)
            filter_page.apply_filters()
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()