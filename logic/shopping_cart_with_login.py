from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from selenium.webdriver.support.select import Select


class ShoppingCartPage(BasePage):
    # QUANTITY_DROP_DOWN = (By.ID, "dropdown-654526507-9a932b78-dad9-4e91-a1d1-74892d845463")
    # REMOVE_BUTTON = (By.XPATH, "//button[@data-test-id='cart-remove-item']")
    QUANTITY_DROP_DOWN = (By.CSS_SELECTOR, "select[data-test-id='qty-dropdown']")
    REMOVE_BUTTON = (By.XPATH, "//button[@data-test-id='cart-remove-item']")

    def update_quantity_to_8(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.QUANTITY_DROP_DOWN)
        )
        Select(self.driver.find_element(*self.QUANTITY_DROP_DOWN)).select_by_value("8")

    def remove_item(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REMOVE_BUTTON)
        ).click()
