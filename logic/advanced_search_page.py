from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class AdvancedSearchPage(BasePage):
    ITEM_ID_INPUT = (By.ID, "_nkw")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit'][contains(@data-track, 'Search')]")
    ITEM_IMG = (By.XPATH, "//img[contains(@src, 'ebayimg.com')]")
    ADD_TO_WATCHLIST_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'ux-call-to-action')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_item_id_and_search(self, item_id):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ITEM_ID_INPUT)).send_keys(item_id)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def select_first_result_and_add_to_watchlist(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ITEM_IMG)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ADD_TO_WATCHLIST_BUTTON)).click()
