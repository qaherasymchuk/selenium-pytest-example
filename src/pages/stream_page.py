from loguru import logger
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class StreamPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.start_button = (By.XPATH, '//button[@data-a-target="content-classification-gate-overlay-start-watching-button"]')
        self.mute_popup_close = (By.XPATH, '//*[@data-test-selector="muted-segments-alert-overlay-presentation__dismiss-button"]/div')
        self.video_container = (By.XPATH, '//div[@data-test-selector="video-player__video-container"]')
        self.resize_detector = (By.XPATH, '//div[@class="resize-detector"]')

    def close_popups(self):
        if consent_popup_continue := self.wait_for_element_to_be_visible(self.start_button):
            logger.info("Close consent popup")
            self.js_click_on_element(consent_popup_continue)
            self.wait_for_element_disappears(self.start_button)

        if mute_popup_close := self.wait_for_element_to_be_visible(self.mute_popup_close):
            logger.info("Close mute popup")
            self.js_click_on_element(mute_popup_close)
            self.wait_for_element_disappears(self.mute_popup_close)

    def wait_for_video_loading(self):
        video_container = self.wait_for_element_to_be_visible(self.video_container)
        assert video_container.is_displayed(), "Video not loaded"
