from models import User, AdminUser
from manager import UserManager

mgr = UserManager()

u1 = User("mike", "mike@test.com")
u2 = User("sara", "sara@test.com")
a1 = AdminUser("ana", "ana@test.com", permissions=["read", "write"])

mgr.add_user(u1)
mgr.add_user(u2)
mgr.add_user(a1)

print(mgr.find_by_username("mike"))   # User(...)
print(mgr.find_by_username("ghost"))  # None

mgr.deactivate_user("sara")

active = mgr.list_active_users()
for u in active:
    print(u)
