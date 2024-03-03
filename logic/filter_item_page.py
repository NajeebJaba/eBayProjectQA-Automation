from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class FilterItemPage(BasePage):
    RAM_SIZE_CHECKBOX = "//input[@class='checkbox__control' and @aria-label='32 GB']"
    SSD_CAPACITY_CHECKBOX = "//input[@class='checkbox__control' and @aria-label='1 TB']"
    PROCESSOR_CHECKBOX = "//input[@class='checkbox__control' and @aria-label='Apple M2 Max']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkbox(self, checkbox_xpath):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, checkbox_xpath))
        )
        self.driver.execute_script("arguments[0].click();", checkbox)

    def apply_filters(self):
        self.click_checkbox(self.RAM_SIZE_CHECKBOX)
        self.click_checkbox(self.SSD_CAPACITY_CHECKBOX)
        self.click_checkbox(self.PROCESSOR_CHECKBOX)
