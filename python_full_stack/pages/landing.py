import reflex as rx

from .. import navigation
from ..navigation.state import NavState
from ..articles.list import article_public_list_component


def hero_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Welcome to Student Succeed",
                size="9",
                background="linear-gradient(to right, #00C6FB, #005BEA)",
                background_clip="text",
            ),
            rx.text(
                "Empowering International Students for Academic Excellence",
                font_size="xl",
                color="gray.500",
            ),
            rx.hstack(
                rx.link(
                    rx.button("Get Started", size="3", color_scheme="blue"),
                    href=navigation.routes.REGISTER_ROUTE,
                ),
                rx.link(
                    rx.button(
                        "About Us", size="3", color_scheme="gray", variant="outline"
                    ),
                    href=navigation.routes.ABOUT_ROUTE,
                ),
                padding_top="1em",
                spacing="4",
            ),
            padding_y="2em",
            spacing="4",
            align="center",
        ),
        width="100%",
        background="radial-gradient(circle at center, rgba(0,198,251,0.1), transparent)",
        padding="2em",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.vstack(
        rx.icon(icon, size=24, color="blue.500"),
        rx.heading(title, size="5"),
        rx.text(description, color="gray.500", text_align="center"),
        spacing="4",
        align="center",
        padding="2em",
        border="1px solid",
        border_color="gray.200",
        border_radius="lg",
        width="100%",
    )


def features_section() -> rx.Component:
    return rx.vstack(
        rx.heading("Why Choose Student Succeed?", size="7"),
        rx.grid(
            feature_card(
                "graduation-cap",
                "Expert Guidance",
                "Get mentorship from experienced educators",
            ),
            feature_card(
                "book", "Rich Resources", "Access comprehensive study materials"
            ),
            feature_card(
                "users",
                "Community Support",
                "Connect with fellow international students",
            ),
            feature_card(
                "chart-line", "Track Progress", "Monitor your academic growth"
            ),
            columns="4",  # Changed from [2, 2, 4] to "4"
            spacing="4",
            padding="2em",
        ),
        padding_y="2em",
    )


def stats_item(number: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.heading(number, size="8", color="blue.500"),
        rx.text(label, font_size="lg"),
        align="center",
    )


def stats_section() -> rx.Component:
    return rx.vstack(
        rx.grid(
            stats_item("1000+", "Students Helped"),
            stats_item("50+", "Expert Mentors"),
            stats_item("95%", "Success Rate"),
            stats_item("24/7", "Support"),
            columns="2",  # Changed from [1, 2] to "2"
            spacing="4",
            padding="2em",
        ),
        padding_y="2em",
    )


def testimonial_card(text: str, author: str, role: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            f'"{text}"',
            font_size="lg",
            font_style="italic",
            color="gray.800",  # Darker text for better readability
        ),
        rx.text(
            author,
            font_weight="bold",
            color="blue.700",  # Brand color for author name
        ),
        rx.text(
            role,
            color="gray.600",
            font_size="sm",
        ),
        spacing="3",
        align="center",
        padding="2em",
        background="rgba(255, 255, 255, 0.1)",  # Very subtle transparent white
        backdrop_filter="blur(10px)",  # Adds frosted glass effect
        border_radius="lg",
        border="1px solid",
        border_color="whiteAlpha.200",
        _hover={
            "transform": "translateY(-2px)",
            "background": "rgba(255, 255, 255, 0.15)",
            "transition": "all 0.2s ease-in-out",
        },
    )


def testimonials_section() -> rx.Component:
    return rx.vstack(
        rx.heading("What Our Students Say", size="7"),
        rx.grid(
            testimonial_card(
                "Student Succeed helped me adapt to academic life in a new country.",
                "Sarah Chen",
                "International Student",
            ),
            testimonial_card(
                "The mentorship program was invaluable for my success.",
                "Mohammed Ali",
                "Graduate Student",
            ),
            columns="2",
            spacing="4",
            padding="2em",
            background="radial-gradient(circle at center, rgba(0,198,251,0.1), transparent)",  # Subtle background for section
            width="100%",
        ),
        padding_y="2em",
        background="radial-gradient(circle at center, rgba(0,198,251,0.1), transparent)",  # Subtle background for section
        width="100%",
    )


def how_it_works_section() -> rx.Component:
    return rx.vstack(
        rx.heading("How It Works", size="7"),
        rx.grid(
            feature_card("user-plus", "Sign Up", "Create your account and profile"),
            feature_card("users", "Get Matched", "Connect with mentors and resources"),
            feature_card(
                "book-open", "Start Learning", "Access materials and track progress"
            ),
            columns="3",  # Using string for columns as per previous fix
            spacing="4",
            padding="2em",
        ),
        padding_y="2em",
    )


def landing_component() -> rx.Component:
    return rx.vstack(
        hero_section(),
        features_section(),
        stats_section(),
        how_it_works_section(),
        testimonials_section(),
        rx.divider(),
        rx.heading("Recent Articles", size="5"),
        article_public_list_component(columns=1, limit=1),
        spacing="5",
        width="100%",
        align="center",
        min_height="85vh",
        id="my-child",
    )
