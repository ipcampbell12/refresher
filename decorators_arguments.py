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
def get_password(panel):
    if panel == "admin":
        return '1234'
    elif panel == "billing":
        return "super_secure_password"


print(get_password("billing"))
