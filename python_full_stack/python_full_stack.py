"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from .ui.base import base_page
from .pages import about, team


class State(rx.State):
    """The app state."""
    label = "Welcome to AdviseWell !"

    def user_name(self):
        self.label = "Vijay (from a function)."

    def handle_input_changes(self, val):
        self.label = val


def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.input(
                default_value=State.label,
                on_change=State.handle_input_changes
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="stretch",
            text_align = "center",
            id = "my-child",

        )
    return base_page(my_child)

app = rx.App()
app.add_page(index)
app.add_page(about.about_page, route = '/about')
app.add_page(team.team_page, route = '/team')
