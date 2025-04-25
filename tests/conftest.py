import os

import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from src.components.footer import Footer
from src.pages.base_page import BasePage
from src.pages.home_page import HomePage
from src.pages.search_page import SearchPage
from src.pages.stream_page import StreamPage


# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    logger.error(f"\nFailed feature: {feature.name}.\nFailed scenario: {scenario.name}.\nFailed step: {step.name}")
    driver = request.getfixturevalue('driver')
    logger.info("Found page through fixture request")

    if driver:
        file_name = scenario.name.replace(' ', '_')
        logger.info("Page fixture is available. Capture screenshot")
        screenshot_path = f"{os.environ.get('SCREENSHOTS')}/{file_name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(filename=screenshot_path)
        logger.info(f"Screenshot taken for failed test: {screenshot_path}")

        # Save page source
        logger.info("Saving page source")
        html_path = f"{os.environ.get('SCREENSHOTS')}/{file_name}.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        logger.info(f"Page source saved for failed test: {html_path}")
    else:
        logger.error("Page fixture is not available")


# fixtures:

@pytest.fixture(name="configure_logger", scope="package", autouse=True)
def configure_logger_fixture():
    test_output_log_file = f"{os.environ.get('TEST_LOG_DIR_PATH')}/test_output.log"
    if os.path.exists(test_output_log_file):
        os.remove(test_output_log_file)
    logger.add(
        f"{os.environ.get('TEST_LOG_DIR_PATH')}/test_output.log",
        format="{time} {level} {message}",
        level=os.environ.get("TEST_LOG_LEVEL", "INFO"),
        rotation="10 MB"
    )


@pytest.fixture(scope="module")
def driver() -> WebDriver:
    if not (browser := os.environ.get('BROWSER')):
        raise ValueError("Environment variable 'BROWSER' is not set.")

    match browser.lower():
        case "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-tools")
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)
        case "firefox":
            driver = webdriver.Firefox()
        case "ie":
            driver = webdriver.Ie()
        case "safari":
            driver = webdriver.Safari()
        case "mobile_emulator":
            options = webdriver.ChromeOptions()
            mobile_emulation = {"deviceName": "iPhone 12 Pro"}
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            # options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(options=options)
        case _:
            raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def home_page(driver) -> HomePage:
    return HomePage(driver)


@pytest.fixture(scope="module")
def footer(driver) -> Footer:
    return Footer(driver)


@pytest.fixture(scope="module")
def search_page(driver) -> SearchPage:
    return SearchPage(driver)


@pytest.fixture(scope="module")
def stream_page(driver) -> StreamPage:
    return StreamPage(driver)


@pytest.fixture(scope="module")
def base_page(driver) -> BasePage:
    return BasePage(driver)
