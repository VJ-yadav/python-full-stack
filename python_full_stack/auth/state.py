import reflex as rx
import reflex_local_auth

import sqlmodel

from ..models import UserInfo




class SessionState(reflex_local_auth.LocalAuthState):
    @rx.var
    def my_userinfo_id(self) -> str | None:
        if self.authenticated_user_info is None:
            return None
        return str(self.authenticated_user_info.id)

    @rx.var
    def my_user_id(self) -> str | None:
        if self.authenticated_user.id < 0:
            return None
        return str(self.authenticated_user.id)
    
    @rx.var
    def authenticated_username(self) -> str | None:
        if self.authenticated_user.id < 0:
            return None
        return self.authenticated_user.username

    @rx.var
    def authenticated_user_info(self) -> UserInfo | None:
        if self.authenticated_user.id < 0:
            return None
        try:
            with rx.session() as session:
                result = session.exec(
                    sqlmodel.select(UserInfo).where(
                        UserInfo.user_id == self.authenticated_user.id
                    ),
                ).one_or_none()
                return result
        except Exception as e:
            print(f"Error retrieving user info: {e}")
            return None
    
    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        print(self.is_authenticated)
        print(self.authenticated_user_info)

    def perform_logout(self):
        self.do_logout()
        return rx.redirect("/")

    def update_user_info(self, form_data: dict):
        if not self.is_authenticated:
            return rx.window_alert("You must be logged in to update your profile")
        
        try:
            with rx.session() as session:
                user_info = session.exec(
                    sqlmodel.select(UserInfo).where(
                        UserInfo.user_id == self.authenticated_user.id
                    )
                ).one_or_none()
                
                if user_info:
                    for key, value in form_data.items():
                        if hasattr(user_info, key):
                            setattr(user_info, key, value)
                    
                    session.add(user_info)
                    session.commit()
                    return rx.window_alert("Profile updated successfully!")
                return rx.window_alert("User info not found")
        except Exception as e:
            print(f"Error updating user info: {e}")
            return rx.window_alert(f"Error updating profile: {str(e)}")



class MyRegisterState(reflex_local_auth.RegistrationState):
    my_error_message: str = ""
    registration_success: bool = False
    success_message: str = ""
    
    def form_value(self, key: str, default=None):
        """Get a form value."""
        return self.get_form_value(key, default)
    
    def _validate_fields(
        self, username: str, password: str, confirm_password: str, terms_agreed: bool = False
    ) -> rx.event.EventSpec | None:
        """Validate registration fields.

        Args:
            username: The username to validate.
            password: The password to validate.
            confirm_password: The confirmation password to validate.
            terms_agreed: Whether the user agreed to the terms.

        Returns:
            An event to set the error message, or None if validation passes.
        """
        # Validate username
        if len(username) < 3:
            self.my_error_message = "Username must be at least 3 characters"
            return rx.set_value("my_error_message", self.my_error_message)
        
        # Validate password
        if len(password) < 8:
            self.my_error_message = "Password must be at least 8 characters"
            return rx.set_value("my_error_message", self.my_error_message)
        
        # Check if passwords match
        if password != confirm_password:
            self.my_error_message = "Passwords do not match"
            return rx.set_value("my_error_message", self.my_error_message)
        
        # Validate terms agreement
        if not terms_agreed:
            self.my_error_message = "You must agree to the Terms of Service"
            return rx.set_value("my_error_message", self.my_error_message)
        
        return None
        
    def handle_registration(
        self, form_data
    ) -> rx.event.EventSpec | list[rx.event.EventSpec]:
        """Handle registration form on_submit.

        Set error_message appropriately based on validation results.

        Args:
            form_data: A dict of form fields and values.
        """
        username = form_data["username"]
        password = form_data["password"]
        terms_agreed = form_data.get("terms_agreed", False)
        
        # First validate the fields
        validation_errors = self._validate_fields(
            username, password, form_data["confirm_password"], terms_agreed
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        
        # Check if username already exists
        with rx.session() as session:
            from reflex_local_auth.user import LocalUser
            existing_user = session.query(LocalUser).filter(LocalUser.username == username).first()
            if existing_user:
                self.my_error_message = f"Username '{username}' is already taken. Please choose another."
                return rx.set_value("my_error_message", self.my_error_message)
        
        # If we get here, username is available, so register the user
        self._register_user(username, password)
        return rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)
    
    def handle_registration_email(self, form_data):
        """Handle registration with email.
        
        This extends the regular registration by also creating a UserInfo record
        with the provided email address.
        
        Args:
            form_data: A dict of form fields and values.
        """
        result = self.handle_registration(form_data)
        
        # Check if registration was successful
        # If result is an event or list of events, it means registration failed
        if isinstance(result, (list, rx.event.EventSpec)):
            # Registration failed, return the error
            return result
        
        try:
            # Registration was successful, create UserInfo
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["email"],
                        user_id=self.new_user_id,
                    )
                )
                session.commit()
            
            # Set success message and flag
            self.registration_success = True
            self.success_message = f"Registration successful! Welcome, {form_data['username']}!"
            
            # Return events to update UI and redirect
            return [
                rx.set_value("registration_success", True),
                rx.set_value("success_message", self.success_message),
                rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)
            ]
        except Exception as e:
            print(f"Error creating user info: {e}")
            self.my_error_message = f"Registration succeeded but failed to create profile: {str(e)}"
            return rx.set_value("my_error_message", self.my_error_message)
