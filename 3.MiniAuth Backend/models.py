class User:
    def __init__(self, username, email, password, is_active=True):
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        if not isinstance(is_active, bool):
            raise ValueError("is_active must be a boolean")

        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")

        self._username = username
        self._email = email
        self._password = password
        self._is_active = is_active

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def is_active(self):
        return self._is_active

    def deactivate(self):
        self._is_active = False

    def activate(self):
        self._is_active = True

    def change_email(self, new_email):
        if not isinstance(new_email, str):
            raise ValueError("Email must be a string")
        if "@" not in new_email or "." not in new_email:
            raise ValueError("Invalid email")
        self._email = new_email

    def reset_password(self, new_password):
        if not isinstance(new_password, str):
            raise ValueError("The new password must be a string")
        if len(new_password) < 8:
            raise ValueError("The new password must be at least 8 characters")
        if new_password == self._password:
            raise ValueError(
                "The new password must be different from the old one")
        self._password = new_password

    def check_password(self, password):
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        return password == self._password

    def __str__(self):
        return f"User({self._username}, {self._email}, active={self._is_active})"
