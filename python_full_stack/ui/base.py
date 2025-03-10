import reflex as rx
from .nav import navbar
from .sidebar import sidebar_bottom_profile

def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:

    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")

        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-left")
        )

    return rx.fragment(
        navbar(),
        rx.hstack(sidebar_bottom_profile(),
            rx.box(
            child,
            id = "content-box",
            padding="1em",
            width="100%",
        ),
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        id="my-base-container",

    )
