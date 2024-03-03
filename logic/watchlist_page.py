from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WatchlistPage(BasePage):
    VIEW_ALL_ITEMS_LINK = (By.XPATH, "//span[contains(text(), 'View all items you are watching')]")

    def __init__(self, driver):
        super().__init__(driver)

    def view_all_watched_items(self):
        """clicking on the sentence to navigate to the watchlist page"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VIEW_ALL_ITEMS_LINK)
        ).click()
