import reflex as rx
import reflex_local_auth


from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.flex(
                            rx.avatar(fallback="SS", size="4"), #for image, just make a logo  of SS later
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    rx.link(
                        rx.heading(
                            "Student Succeed", size="7", weight="bold"
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    navbar_link("Articles", navigation.routes.ARTICLE_LIST_ROUTE),
                    navbar_link("Schedule TopMate", navigation.routes.PRICING_ROUTE),
                    navbar_link("Contact Us", navigation.routes.CONTACT_US_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Register",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.REGISTER_ROUTE
                    ),
                    rx.link(
                        rx.button(
                            "Login",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.LOGIN_ROUTE
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id='my-navbar-hstack-desktop',
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(rx.link(
                        rx.flex(
                            rx.avatar(fallback="SS", size="4"), #for image, just make a logo  of SS later
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    rx.heading(
                        "Student Succeed", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", 
                            on_click=navigation.NavState.to_home),
                        rx.menu.item("About", 
                            on_click=navigation.NavState.to_about_us),
                        rx.menu.item("Articles", 
                            on_click=navigation.NavState.to_articles),
                        rx.menu.item("Schedule TopMate", 
                            on_click=navigation.NavState.to_pricing),
                        rx.menu.item("Contact Us", 
                            on_click=navigation.NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in", 
                            on_click=navigation.NavState.to_login),
                        rx.menu.item("Register", 
                            on_click=navigation.NavState.to_register),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("jade", 7),
        padding="1em",
        width="100%",
        id='my-main-nav',
    )