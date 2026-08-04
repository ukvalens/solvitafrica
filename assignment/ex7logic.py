age=22
has_id = True
allowed=(age >= 19) and has_id
print("Allowed to enter the club:", allowed)
allowed=(age >= 19) or has_id
print("Allowed to enter the club:", allowed)
not_allowed=not has_id
print("Not allowed to enter the club:", not_allowed)