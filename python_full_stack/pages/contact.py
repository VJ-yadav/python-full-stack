import reflex as rx
from ..ui.base import base_page
from .. import contact

def contact_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contact US", size="9"),
            rx.cond(contact.ContactState.did_submit, contact.ContactState.thankyou,""),
            rx.desktop_only(
                rx.box(contact.contact_form(),
                       id = 'my-form-box',
                       width = '50vw',
                       )
            ),
            rx.mobile_and_tablet(
                rx.box(contact.contact_form())
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            text_align = "center",
            id = "contact-page",

        )
    return base_page(my_child) 