import reflex as rx
from ..ui.base import base_page
import asyncio

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    

    @rx.var
    def thankyou(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"


    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        self.did_submit = True

def contact_page() -> rx.Component:
    # Welcome Page (Index)
    my_form = rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="first_name",
                        placeholder="First Name",
                        required=True,
                        width = '100%',
                    ),
                    rx.input(
                        name="middle_name",
                        placeholder="Middle Name",
                        required=False,
                        width = '100%',
                    ),
                    rx.input(
                        name="last_name",
                        placeholder="Last Name",
                        required=True,
                        width = '100%',
                    ),
                    width = '100%',
                ),
                rx.input(
                    name="email",
                    type="email",
                    placeholder='Your Email',
                    required=True,
                    width = '100%',
                ),
                
                rx.text_area(
                    name = 'message',
                    placeholder='Your message',
                    width = '100%',
                ),
                rx.button("Submit", type="submit"),
            ),
                on_submit=ContactState.handle_submit,
                reset_on_submit=True,
            ),
    
    my_child = rx.vstack(
            rx.heading("Contact US", size="9"),
            rx.cond(ContactState.did_submit, ContactState.thankyou,""),
            rx.desktop_only(
                rx.box(my_form,
                       id = 'my-form-box',
                       width = '50vw',
                       )
            ),
            rx.mobile_and_tablet(
                rx.box(my_form)
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            text_align = "center",
            id = "contact-page",

        )
    return base_page(my_child) 