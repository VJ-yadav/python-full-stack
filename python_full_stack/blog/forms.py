import reflex as rx
from typing import Optional

from .state import BlogAddPostFormState, BlogEditFormState


def blog_post_add_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    name="title",
                    placeholder="Title",
                    required=True,
                    type="text",
                    width="100%",
                ),
                width="100%",
            ),
            rx.text_area(
                name="content",
                placeholder="Your message",
                required=True,
                height="50vh",
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=BlogAddPostFormState.handle_submit,
        reset_on_submit=True,
    )


def blog_post_edit_form() -> rx.Component:
    post = BlogEditFormState.post
    if post is None:
        return rx.text("No Post Found.")

    # Define values with proper typing
    post_id: Optional[str] = str(post.id) if post.id is not None else None
    title: Optional[str] = post.title if post.title is not None else ""
    post_content: str = str(
        BlogEditFormState.post_content
        if BlogEditFormState.post_content is not None
        else ""
    )

    return rx.form(
        rx.box(
            rx.input(
                type="hidden",
                name="post_id",
                value=post_id,
                is_required=False,
            ),
            display="none",
        ),
        rx.vstack(
            rx.hstack(
                rx.input(
                    default_value=title,
                    name="title",
                    placeholder="Title",
                    required=True,
                    type="text",
                    width="100%",
                ),
                width="100%",
            ),
            rx.text_area(
                value=post_content,
                on_change=BlogEditFormState.set_post_content,
                name="content",
                placeholder="Your message",
                required=True,
                height="50vh",
                width="100%",
            ),
            rx.flex(
                rx.switch(
                    default_checked=BlogEditFormState.post_publish_active,
                    on_change=BlogEditFormState.set_post_publish_active,
                    name="publish_active",
                ),
                rx.text("Publish Active"),
                spacing="2",
            ),
            rx.cond(
                BlogEditFormState.post_publish_active,
                rx.box(
                    rx.hstack(
                        rx.input(
                            default_value=BlogEditFormState.publish_display_date,
                            type="date",
                            name="publish_date",
                            width="100%",
                        ),
                        rx.input(
                            default_value=BlogEditFormState.publish_display_time,
                            type="time",
                            name="publish_time",
                            width="100%",
                        ),
                        width="100%",
                    ),
                    width="100%",
                ),
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=BlogEditFormState.handle_submit,
    )
