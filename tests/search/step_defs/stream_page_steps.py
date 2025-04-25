from pytest_bdd import when

from src.pages.stream_page import StreamPage


@when("close any popups before start video")
def step_impl(stream_page: StreamPage):
    stream_page.close_popups()


@when("wait until video is loaded")
def step_impl(stream_page: StreamPage):
    stream_page.wait_for_video_loading()
