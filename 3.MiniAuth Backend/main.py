from services import AuthService

service = AuthService()


def run(title, fn):
    print(f"\n=== {title} ===")
    try:
        result = fn()
        print("OK:", result)
    except ValueError as e:
        print("ERROR:", e)


# 1) Register users
run("Register ana", lambda: service.register_user(
    "ana", "ana@test.com", "password123"))
run("Register mike", lambda: service.register_user(
    "mike", "mike@test.com", "password123"))

# 2) Duplicate register
run("Register duplicate ana", lambda: service.register_user(
    "ana", "dup@test.com", "password123"))

# 3) Login success
run("Login ana success", lambda: service.login("ana", "password123"))

# 4) Login wrong password
run("Login ana wrong password", lambda: service.login("ana", "wrongpass"))

# 5) Deactivate + idempotent deactivate
run("Deactivate ana", lambda: service.deactivate_user("ana"))
run("Deactivate ana again (idempotent)", lambda: service.deactivate_user("ana"))

# 6) Login inactive user
run("Login ana inactive", lambda: service.login("ana", "password123"))

# 7) Reset password inactive user
run("Reset password ana inactive",
    lambda: service.reset_password("ana", "newpass123"))

# 8) Activate + reset password
run("Activate ana", lambda: service.activate_user("ana"))
run("Reset password ana (valid)",
    lambda: service.reset_password("ana", "newpass123"))

# 9) Reset password to same password (domain invariant)
run("Reset password ana same again",
    lambda: service.reset_password("ana", "newpass123"))

# 10) Login with new password
run("Login ana with new password", lambda: service.login("ana", "newpass123"))

# 11) Not found cases
run("Deactivate ghost", lambda: service.deactivate_user("ghost"))
run("Login ghost", lambda: service.login("ghost", "password123"))
