import reflex as rx
from . import routes
import reflex_local_auth


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
    
    def to_register(self):
        return rx.redirect(reflex_local_auth.routes.REGISTER_ROUTE)
    def to_login(self):
        return rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)