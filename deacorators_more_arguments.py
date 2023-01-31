import functools

user = {"username": "jeff", "access_level": "guest"}

# USE ARGS AND KWARGS IN CASE FUNCTIONS TAKE ARGUMENTS
# THIS IS FOR DECORATING FUNCTION WITH PARAMETERS


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)

    return secure_function


@make_secure
def get_admin_password(panel):
    return "admin: 1234"


@make_secure
def get_dashboard_password(panel):
    return "user: user_password"
