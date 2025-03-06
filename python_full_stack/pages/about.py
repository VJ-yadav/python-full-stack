import reflex as rx
from ..ui.base import base_page

def about_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("About us", size="9"),
            rx.text(
                "this is About us page",
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="stretch",
            text_align = "center",
            id = "about-page",

        )
    return base_page(my_child)