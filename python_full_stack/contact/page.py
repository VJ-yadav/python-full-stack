import reflex as rx
from ..ui.base import base_page

from . import state
from . import form
 



def contact_entries_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="9"), 
            spacing="5",
            min_height="85vh",
            align="center",
            text_align = "center",
        )
    )

def contact_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contact US", size="9"),
            rx.cond(state.ContactState.did_submit, state.ContactState.thankyou,""),
            rx.desktop_only(
                rx.box(form.contact_form(),
                       id = 'my-form-box',
                       width = '50vw',
                       )
            ),
            rx.mobile_and_tablet(
                rx.box(form.contact_form())
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            text_align = "center",
            id = "contact-page",

        )
    return base_page(my_child) 
