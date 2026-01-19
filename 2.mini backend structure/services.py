from models import User


class UserService:
    def __init__(self):
        self._users = []

    def register_user(self, username, email, is_active=True):
        if self.find_by_username(username) is not None:
            raise ValueError("Username already exists")

        user = User(username, email, is_active)
        self._users.append(user)
        return user

    def deactivate_user(self, username):
        user = self.find_by_username(username)

        if user is None:
            raise ValueError("User not found")

        if not user.is_active:
            return user

        user.deactivate()
        return user

    def find_by_username(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None
