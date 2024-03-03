from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    SIGN_IN_LINK = (By.XPATH, "//a[text()='Sign in']")

    SEARCH_BAR = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")

    WATCHLIST_LINK = (By.XPATH, "//a[@title='Watchlist']")

    SHOP_BY_CATEGORY_LINK = (By.ID, "gh-shop-a")

    CART_ICON = (By.XPATH, "//a[contains(@href, 'cart.payments.ebay.com/sc/view')]")

    ADVANCED_LINK = (By.ID, "gh-as-a")

    def __init__(self, driver):
        super().__init__(driver)

        """check if it's correct"""
        # self.url = url

    def click_on_sign_in_link(self):
        self.driver.find_element(*self.SIGN_IN_LINK).click()

    def navigate_to_home_page(self):
        self.driver.get(self.url)

    def search_for_item(self, item_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BAR)
        )
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(item_name + Keys.RETURN)

    def watchlist_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WATCHLIST_LINK)
        ).click()

    def click_shop_by_category(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHOP_BY_CATEGORY_LINK)
        ).click()

    def click_cart_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def click_advanced_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADVANCED_LINK)).click()
