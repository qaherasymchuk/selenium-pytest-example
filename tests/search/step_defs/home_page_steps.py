from pytest_bdd import given, when

from src.components.footer import Footer
from src.pages.home_page import HomePage


@given("Twitch home page is opened")
def step_impl(home_page: HomePage):
    home_page.open()


@when("user accept cookies and advertising choices")
def step_impl(home_page: HomePage):
    home_page.accept_cookies()


@when("open search page")
def step_impl(footer: Footer):
    footer.open_search_page()
