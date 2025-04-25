from loguru import logger
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logo = (By.XPATH, '//*[@interactioncontent="logo"]')

    def open(self):
        logger.info("Opening Home page")
        self.driver.get(self.base_url)

    def verify_page_is_opened(self):
        self.wait_for_element_to_be_visible(self.logo)
