import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.base_page.home_page import HomePage
from logic.shop_by_category import ShopByCategoryPage
from infra.config_handler import ConfigHandler
import concurrent.futures
import time

class ParallelShopByCategoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config

    def run_shop_by_category_test_on_browser(self, browser_name):
        print(f"Running shop by category test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)
            category_page = ShopByCategoryPage(driver)
            home_page.click_shop_by_category()
            category_page.select_sporting_goods()
            time.sleep(3)
            category_page.select_team_sports()
            category_page.select_soccer()
            category_page.select_balls()
            category_page.select_ball_size_5()
            time.sleep(4)
            assert "Soccer Balls Size 5" in driver.title

        finally:
            driver.quit()

    def test_parallel_shop_by_category(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_shop_by_category_test_on_browser, browser): browser for browser in self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Shop by category test completed on {browser}')

if __name__ == "__main__":
    unittest.main()
