import os

from pytest_bdd import when, parsers, then
from selenium.webdriver.common.selenium_manager import logger

from src.pages.base_page import BasePage


@when(parsers.cfparse("save screenshot and page source as {file_name} file"))
def step_impl(file_name: str, base_page: BasePage):
    screenshot_path = f"{os.environ.get('SCREENSHOTS')}/{file_name}.png"
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    base_page.driver.save_screenshot(filename=screenshot_path)

    logger.info("Saving page source")
    html_path = f"{os.environ.get('SCREENSHOTS')}/{file_name}.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(base_page.driver.page_source)


@then(parsers.cfparse("{file_name} screenshot and page source files are present"))
def step_impl(file_name):
    screenshot_path = f"{os.environ.get('SCREENSHOTS')}/{file_name}.png"
    page_source_path = f"{os.environ.get('SCREENSHOTS')}/{file_name}.html"
    assert os.path.exists(screenshot_path), f"Screenshot {file_name} does not exist"
    assert os.path.exists(page_source_path), f"Page source {file_name} does not exist"