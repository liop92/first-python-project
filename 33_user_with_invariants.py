class User:
    def __init__(self, username, email, is_active=True):
        if len(username) >= 3:
            self._username = username
        else:
            raise ValueError("Username must be at least 3 characters")
        if "@" in email and "." in email:
            self._email = email
        else:
            raise ValueError("Invalid email")
        if isinstance(is_active, bool):
            self._is_active = is_active
        else:
            raise ValueError("is_active must be a boolean")

    def deactivate(self):
        self._is_active = False

    def activate(self):
        self._is_active = True

    def change_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
        else:
            raise ValueError("Invalid email")

    def __str__(self):
        return f"User({self._username}, {self._email}, active={self._is_active})"
