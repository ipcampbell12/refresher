def divide(dividend, divisor):

    if divisor == 0:

        raise ZeroDivisionError(" Divisor cannot be 0")

    return dividend/divisor

# *values tuple takes in any number of arguments


def calculate(*values, operator):
    # calls operator function with values
    # parentheses indicate that operator must be a function
    return operator(*values)


# first class function: functions are variables, can be passed in as arguments to other functions

# passes in divide function as operator
# divide function is not called (i.e. not ()), just used as a value
# adding parenthese means python won't recognize it as a positional argument

result = calculate(20, 4, operator=divide)

print(result)
