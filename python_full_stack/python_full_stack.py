import reflex as rx


from rxconfig import config
from .ui.base import base_page
from . import blog, contact, navigation, pages

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

app.add_page(pages.about_page, 
             route = navigation.routes.ABOUT_ROUTE)

app.add_page(pages.team_page, 
             route = navigation.routes.TEAM_ROUTE)

app.add_page(blog.blog_post_edit_page, 
             route = "blog/[blog_id]/edit",
             on_load=blog.BlogPostState.get_post_detail,
             )

app.add_page(blog.blog_post_detail_page, 
             route = "blog/[blog_id]",
             on_load=blog.BlogPostState.get_post_detail,
             )

app.add_page(blog.blog_post_list_page, 
             route = navigation.routes.BLOG_POSTS_ROUTE,
             on_load = blog.BlogPostState.load_posts)

app.add_page(blog.blog_post_add_page, 
             route = navigation.routes.BLOG_POSTS_ADD_ROUTE,
             )

app.add_page(contact.contact_page, 
             route = navigation.routes.CONTACT_ROUTE)
app.add_page(
    contact.contact_entries_list_page, 
    route = navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
    )
