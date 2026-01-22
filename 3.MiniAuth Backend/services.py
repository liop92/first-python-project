from models import User


class AuthService:
    def __init__(self):
        self._users = []

    def find_by_username(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None

    def register_user(self, username, email, password):
        if self.find_by_username(username) is not None:
            raise ValueError("Username already exists")

        user = User(username, email, password)
        self._users.append(user)
        return user

    def login(self, username, password):
        user = self.find_by_username(username)
        if user is None:
            raise ValueError("User not found")

        if not user.is_active:
            raise ValueError("User is inactive")

        if not user.check_password(password):
            raise ValueError("Invalid password")

        return user

    def deactivate_user(self, username):
        user = self.find_by_username(username)

        if user is None:
            raise ValueError("User not found")

        if not user.is_active:
            return user

        user.deactivate()
        return user

    def activate_user(self, username):
        user = self.find_by_username(username)

        if user is None:
            raise ValueError("User not found")

        if user.is_active:
            return user

        user.activate()
        return user

    def reset_password(self, username, new_password):
        user = self.find_by_username(username)

        if user is None:
            raise ValueError("User not found")

        if not user.is_active:
            raise ValueError("User is inactive")

        user.reset_password(new_password)
        return user
