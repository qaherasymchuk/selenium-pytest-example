"""
Login feature step definitions.
"""
from pytest_bdd import scenarios
from .step_defs.common_steps import *
from .step_defs.home_page_steps import *
from .step_defs.search_page_steps import *
from .step_defs.stream_page_steps import *

scenarios('./features/streamer_page_screenshot.feature')

