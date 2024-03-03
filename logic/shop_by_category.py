from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class ShopByCategoryPage(BasePage):
    SPORTING_GOODS_LINK = (By.XPATH, "//a[contains(@href, '/b/Sporting-Goods/888')]")
    TEAM_SPORTS_TEXT = (By.XPATH, "//span[contains(text(), 'Team Sports')]")
    SOCCER_LINK = (By.XPATH, "//a[contains(@href, '/b/Soccer/20862/bn_1941947')]")
    BALLS_IMAGE = (By.XPATH, "//img[@alt='Balls']")
    BALL_SIZE_5_LINK = (By.XPATH, "//a[contains(@href, 'Ball%2520Size=5')]//p[text()='5']")
    def __init__(self, driver):
        super().__init__(driver)

    def select_sporting_goods(self):
        self.driver.find_element(*self.SPORTING_GOODS_LINK).click()

    def select_team_sports(self):
        self.driver.find_element(*self.TEAM_SPORTS_TEXT).click()

    def select_soccer(self):
        self.driver.find_element(*self.SOCCER_LINK).click()

    def select_balls(self):
        self.driver.find_element(*self.BALLS_IMAGE).click()

    def select_spoorting_goods(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SPORTING_GOODS_LINK)
        ).click()

    def select_ball_size_5(self, BALL_SIZE_5=None):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.BALL_SIZE_5_LINK)
        ).click()

