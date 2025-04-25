from loguru import logger
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class Footer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_button = (By.XPATH, '//*[@href="/"]')
        self.browse_button = (By.XPATH, '//*[@href="/directory"]')
        self.activity_button = (By.XPATH, '//*[@href="/activity"]')
        self.profile_button = (By.XPATH, '//*[@href="/home"]')

    def open_search_page(self):
        logger.info("Opening search page")
        self.wait_for_element_to_be_visible(self.browse_button).click()
