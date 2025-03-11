import reflex as rx

from reflex_local_auth.pages import login_page
from ..ui.base import base_page


def my_login_page():
    return base_page(
        login_page
    )
