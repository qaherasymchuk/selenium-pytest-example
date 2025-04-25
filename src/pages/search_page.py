from loguru import logger
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = (By.XPATH, '//*[@type="search"]')
        self.search_options = (By.XPATH, '//ul/li//p')
        self.top_results_tab = (By.XPATH, '//li[@role="presentation"][1]/a')
        self.channel_results_tab = (By.XPATH, '//li[@role="presentation"][2]/a')
        self.categories_results_tab = (By.XPATH, '//li[@role="presentation"][3]/a')
        self.videos_results_tab = (By.XPATH, '//li[@role="presentation"][4]/a')
        self.videos = (By.XPATH, '//a[contains(@class, "ScCoreLink")]')

    def search(self, search_string):
        logger.info(f"Searching for '{search_string}'")
        search_input = self.wait_for_element_to_be_clickable(self.search_input)
        search_input.click()
        search_input.send_keys(search_string)

        elements = self.wait_for_all_elements_to_be_visible(self.search_options)
        assert elements[0].is_displayed(), "No result dropdown"
        self.js_click_on_element(elements[0])

    def open_last_streamer(self):
        logger.info("Opening last streamer")
        videos = self.wait_for_all_elements_to_be_visible(self.videos)
        self.wait.until(lambda _ : len(videos) > 0)
        last_video = videos[-1]
        self.js_click_on_element(last_video)

    def switch_to_results_category(self, results_category):
        match results_category.lower():
            case "top":
                element = self.wait_for_element_to_be_clickable(self.top_results_tab)
            case "channels":
                element = self.wait_for_element_to_be_clickable(self.channel_results_tab)
            case "categories":
                element = self.wait_for_element_to_be_clickable(self.categories_results_tab)
            case "videos":
                element = self.wait_for_element_to_be_clickable(self.videos_results_tab)
            case _:
                raise ValueError(f"Unknown result category '{results_category}'")
        self.js_click_on_element(element)
        element.click()
        self.wait.until(
            lambda _: element.get_attribute("aria-selected") == "true"
        )


