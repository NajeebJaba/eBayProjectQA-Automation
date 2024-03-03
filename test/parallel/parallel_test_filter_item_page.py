import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.filter_item_page import FilterItemPage
from infra.config_handler import ConfigHandler
import concurrent.futures
import time

class ParallelFilterItemTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.search_item = cls.config["search_item"]

    def run_filter_item_test_on_browser(self, browser_name):
        print(f"Running filter item test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)
            filter_page = FilterItemPage(driver)
            home_page.navigate_to(self.config["url"])
            home_page.search_for_item(self.search_item)
            filter_page.apply_filters()
            time.sleep(5)
            expected_filter_text = "32GB"
            assert expected_filter_text in driver.current_url, "Filter not found in URL"

        finally:
            driver.quit()

    def test_parallel_filter_item(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_filter_item_test_on_browser, browser): browser for browser in self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Filter item test completed on {browser}')

if __name__ == "__main__":
    unittest.main()
