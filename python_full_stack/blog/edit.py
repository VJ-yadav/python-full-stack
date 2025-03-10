import reflex as rx
from . import state

from ..ui.base import base_page
from .state import BlogEditFormState

from . import forms

def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post
    my_child = rx.vstack(
            rx.heading("Editing ", post.title, size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width = '50vw',
                )
            ),
            rx.mobile_only(
                  rx.box(
                    my_form,
                    width='95vw'
                  )
            ),
            rx.tablet_only(
                  rx.box(
                    my_form,
                    width='75vw'
                  )
            ),
            spacing="5",
            min_height="95vh",
            align="center",
            text_align = "center",
        )
    
    return base_page(my_child) 