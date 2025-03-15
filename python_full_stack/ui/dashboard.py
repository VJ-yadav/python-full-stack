import reflex as rx

from .sidebar import sidebar

def base_dashboard_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child,rx. Component):
        child = rx.heading("this is not a valid child element")
    return rx.fragment(
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                padding="1em",
                width="100%",
                id="my-content-area-el"
            ),
            
        ),
    )