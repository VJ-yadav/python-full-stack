import reflex as rx
import reflex_local_auth
from reflex_local_auth.pages.components import MIN_WIDTH

from .state import MyRegisterState

def register_error() -> rx.Component:
    """Render the registration error message."""
    return rx.cond(
        MyRegisterState.my_error_message != "",
        rx.callout(
            MyRegisterState.my_error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )

def my_register_form() -> rx.Component:
    """Render the registration form with improved validation."""
    return rx.form(
        rx.vstack(
            rx.heading("Create an account", size="7"),
            register_error(),
            rx.text("Username"),
            rx.input(
                name="username",
                placeholder="Choose a username (min 3 characters)",
                width="100%",
            ),
            rx.text("Email"),
            rx.input(
                name="email",
                type='email',
                placeholder="Your email address",
                width="100%",
            ),
            rx.text("Password"),
            rx.input(
                name="password",
                type="password",
                placeholder="Min 8 characters with letters and numbers",
                width="100%",
            ),
            rx.text("Confirm Password"),
            rx.input(
                name="confirm_password",
                type="password",
                placeholder="Repeat your password",
                width="100%",
            ),
            rx.checkbox("I agree to the Terms of Service", name="terms_agreed"),
            rx.button("Sign up", width="100%", type="submit"),
            rx.center(
                rx.link("Already have an account? Login", on_click=lambda: rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)),
                width="100%",
            ),
            min_width=MIN_WIDTH,
        ),
        on_submit=MyRegisterState.handle_registration_email,
    )
