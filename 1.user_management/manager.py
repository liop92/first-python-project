class UserManager:
    def __init__(self):
        self._users = []

    def add_user(self, user):
        if self.find_by_username(user.username) is not None:
            raise ValueError("Username already exists")
        self._users.append(user)

    def find_by_username(self, username):
        for u in self._users:
            if u.username == username:
                return u
        return None

    def deactivate_user(self, username):
        user = self.find_by_username(username)
        if user is None:
            raise ValueError("User not found")
        user.deactivate()

    def list_active_users(self):
        active_users = []
        for u in self._users:
            if u.is_active:
                active_users.append(u)
        return active_users
