import functools

user = {"username": "jeff", "access_level": "guest"}

# need to create function that will return the decorator and allow us to check for the access level

# decorator factory


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function
    return decorator

# call the decorator factory, which returns a decorator and applies it to this function
# allows you to pass parameters


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


# these won't allow access
print(get_admin_password())
print(get_dashboard_password())

user = {"username": "stephonica", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
