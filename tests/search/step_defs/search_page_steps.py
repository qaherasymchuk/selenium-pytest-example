from pytest_bdd import when, parsers

from src.pages.search_page import SearchPage


@when(parsers.cfparse('search for "{search_string}"'))
def step_impl(search_string, search_page: SearchPage):
    search_page.search(search_string)


@when(parsers.cfparse("scroll down {scroll_number:d} times"))
def step_impl(scroll_number, search_page: SearchPage):
    search_page.scroll_given_amount(number=scroll_number)


@when("select one streamer")
def step_impl(search_page: SearchPage):
    search_page.open_last_streamer()


@when(parsers.cfparse("switch to {results_category}"))
def step_impl(results_category, search_page: SearchPage):
    search_page.switch_to_results_category(results_category)
