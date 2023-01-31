import functools

user = {"username": "jeff", "access_level": "guest"}


# decorators allow us to easily modify functions


# nothing in this function to prevent guest from accessing admin password
# we want to secure this function
# if statements can protect call, but not function itself
# can do if statement inside function, but then would have to do that for every function


# first class function - takes in a function and returns a function
# get_admin_password is passed to make secure function
# replaces original funciton with secure one
def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function

# place @ on top of function def, prevent function from being created without first getting passed through decorator


@make_secure
def get_admin_password():
    return '1234'

# will return None, can't run None
# would have to make sure user is an admin to run any of our code
# need something that check's user's access level when you call the function, not when you define it


# PROBLEM: with decorators, name of function is replace (name of get_admin_fucntion is now secure_function)
# need functools module, tell secure_function that it is a wrapper for func, the name will persist, need this for most

# @syntax is the same as this
#get_admin_password = secure_function(get_admin_password)


print(get_admin_password())
