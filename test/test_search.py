import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from infra.config_handler import ConfigHandler
import concurrent.futures
import time


class ParallelSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.search_item = cls.config["search_item"]

    def run_search_test_on_browser(self, browser_name):
        print(f"Running search test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)

            home_page.navigate_to(self.config["url"])
            home_page.search_for_item(self.search_item)
            time.sleep(5)
            assert self.search_item.lower() in driver.title.lower()
        finally:
            driver.quit()

    def test_parallel_search(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_search_test_on_browser, browser): browser for browser in
                       self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Search test completed on {browser}')


if __name__ == "__main__":
    unittest.main()
