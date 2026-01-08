class User:
    def __init__(self, username, email, active=True):
        if len(username) >= 3:
            self._username = username
        else:
            raise ValueError("Username must be at least 3 characters")
        if "@" in email and "." in email:
            self._email = email
        else:
            raise ValueError("Invalid email")
        self._active = active

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def is_active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def __str__(self):
        return f"User({self.username}, {self.email}, active={self.is_active})"


class AdminUser(User):
    def __init__(self, username, email, permissions=None, active=True):
        super().__init__(username, email, active)
        if permissions is None:
            self._permissions = []
        else:
            self._permissions = list(permissions)

    @property
    def permissions(self):
        return list(self._permissions)

    def add_permission(self, permission):
        if permission not in self._permissions:
            self._permissions.append(permission)

    def remove_permission(self, permission):
        if permission not in self._permissions:
            raise ValueError("Permission not found")
        self._permissions.remove(permission)

    def __str__(self):
        return f"AdminUser({self.username}, {self.email}, active={self.is_active}, permissions={len(self._permissions)})"
