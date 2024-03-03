from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.search_bar_id = "gh-ac"
        self.search_button_id = "gh-btn"

    def search_for_item(self, item_name):
        # wait up to 10 seconds for the search bar to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.search_bar_id))
        )
        search_bar = self.driver.find_element(By.ID, self.search_bar_id)
        search_bar.clear()  # clear the search bar before typing
        search_bar.send_keys(item_name)
        search_bar.send_keys(Keys.RETURN)