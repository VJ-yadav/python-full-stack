import reflex as rx
from ..ui.base import base_page

from .. import navigation
from . import state, model
 

def blog_post_detail_link(child: rx.Component , post: model.BlogPostModel):
    if post is None:
        return rx.fragment(child)    
    post_id = post.id
    if post_id is None:
        return rx.fragment(child)
    root_path = navigation.routes.BLOG_POSTS_ROUTE
    post_detail_link = f"{root_path}/{post_id}"
    return rx.link(
        child,
        href=post_detail_link
    )


def blog_post_list_item(post: model.BlogPostModel):
    return rx.box(
        blog_post_detail_link(
            rx.heading(post.title),
            post,
    ),padding = '1em',
    )

def blog_post_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts", size="9"), 
            rx.foreach(state.BlogPostState.posts, blog_post_list_item),
            spacing="5",
            min_height="85vh",
            align="center",
            text_align = "center",
        )
    )