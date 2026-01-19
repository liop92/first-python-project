from services import UserService

service = UserService()

# Boundary payloads (simulate requests)
payloads = [
    {"username": "ana", "email": "ana@test.com", "is_active": "true"},
    {"username": "mike", "email": "mike@test.com", "is_active": "false"},
    {"username": "ana", "email": "dup@test.com", "is_active": "true"},  # duplicate
]


def parse_bool(value):
    # boundary parsing
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        v = value.strip().lower()
        if v in ("true", "1", "yes"):
            return True
        if v in ("false", "0", "no"):
            return False
    raise ValueError("Invalid boolean value")


for p in payloads:
    try:
        is_active = parse_bool(p["is_active"])
        user = service.register_user(p["username"], p["email"], is_active)
        print("CREATED:", user)
    except Exception as e:
        print("ERROR:", e)

print("\n--- Deactivate flow ---")
try:
    user = service.deactivate_user("mike")
    print("DEACTIVATED:", user)
    user = service.deactivate_user("mike")  # idempotent
    print("DEACTIVATED AGAIN:", user)
except Exception as e:
    print("ERROR:", e)

print("\n--- Not found ---")
try:
    service.deactivate_user("ghost")
except Exception as e:
    print("ERROR:", e)
