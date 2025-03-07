import reflex as rx
from ..ui.base import base_page

def contact_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Contact US", size="9"),
            rx.text(
                "this is our Contact Page",
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="stretch",
            text_align = "center",
            id = "contact-page",

        )
    return base_page(my_child)