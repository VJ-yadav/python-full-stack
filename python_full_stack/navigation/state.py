import reflex as rx
from . import routes


class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    def to_about(self):
        return rx.redirect(routes.ABOUT_ROUTE)
    def to_team(self):
        return rx.redirect(routes.TEAM_ROUTE)
    def to_blog(self):
        return rx.redirect(routes.BLOG_POSTS_ROUTE)
    def to_add_blog(self):
        return rx.redirect(routes.BLOG_POSTS_ADD_ROUTE)
    def to_create_blog(self):
        return self.to_add_blog()
    def to_contact(self):
        return rx.redirect(routes.CONTACT_ROUTE)