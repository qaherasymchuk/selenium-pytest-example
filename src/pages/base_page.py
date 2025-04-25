import os
import time

from loguru import logger
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import DEFAULT_TIMEOUT
ignored_exceptions = [NoSuchElementException, ElementNotInteractableException]


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=DEFAULT_TIMEOUT, ignored_exceptions=ignored_exceptions)
        self.base_url = os.environ.get('BASE_URL')
        self.accept_cookies_button = (By.XPATH, '//*[@data-a-target="consent-banner-accept"]')
        self.footer = (By.XPATH, '//*[@id="root"]/div[2]')

    def wait_for_element_to_be_visible(self, locator: tuple[str, str]) -> WebElement:
        logger.debug(f"Waiting for element to be visible: {locator}")
        try:
            return self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return None

    def wait_for_element_to_be_clickable(self, locator: tuple[str, str]) -> WebElement:
        logger.debug(f"Waiting for element to be visible: {locator}")
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_all_elements_to_be_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        logger.debug(f"Waiting for all elements to be visible: {locator}")
        return self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))

    def wait_for_element_disappears(self, locator: tuple[str, str]):
        logger.debug(f"Waiting for element to be disappears: {locator}")
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    def filter_elements_by_text(self, locator: tuple[str, str], filter_match: str) -> WebElement:
        logger.debug(f"Filtering elements by text: {filter_match}")
        elements = self.wait_for_all_elements_to_be_visible(locator)
        filter_result = [element for element in elements if element.text == filter_match]
        assert len(filter_result) > 0
        logger.debug(f"Filtered elements count: {len(filter_result)}")
        return self.wait_for_element_to_be_visible(locator)

    def scroll_into_view(self, locator: tuple[str, str]) -> None:
        logger.debug(f"Scrolling into view of element by locator: {locator}")
        element = self.wait_for_element_to_be_visible(locator)
        ActionChains(self.driver) \
            .scroll_to_element(element) \
            .perform()

    def scroll_to_element(self, element: WebElement) -> None:
        logger.debug(f"Scrolling into view of element by element: {element}")
        ActionChains(self.driver) \
            .scroll_to_element(element) \
            .perform() \

    def scroll_given_amount(self, number: int) -> None:
        logger.debug(f"Scrolling down by {number} screen(s)")
        for i in range(number):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            logger.debug(f"Scrolled down {i + 1} time(s)")
            time.sleep(0.5)  # Optional: Add a small delay for smoother scroll effect

    def js_click_by_locator(self, locator: tuple[str, str]):
        element = self.wait_for_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def js_click_on_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].click();", element)

    def accept_cookies(self):
        logger.info('Accept Cookies')
        self.wait_for_element_to_be_visible(self.accept_cookies_button).click()
