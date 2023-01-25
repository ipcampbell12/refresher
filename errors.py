
# This is not the optimal way to handle errors
# def divide(dividend, divisor):

#     if divisor == 0:
#         print("Divisor cannot be 0")

#     return dividend/divisor


# grades = [78, 99, 85, 100]


# Errors are often used for flow contorl
# raise errors in order to catch and handle
# Exception = error

def divide(dividend, divisor):

    if divisor == 0:

        raise ZeroDivisionError(" Divisor cannot be 0")

    return dividend/divisor


grades = []

print("Welcome to the average grade program")

try:
    average = divide(sum(grades), len(grades))

except ZeroDivisionError as e:

    print("There are no grades yet")

else:
    print(f"The average grade is {average}")

finally:
    print("Good bye now!")


# Type error: somethign had the wrong type
# Value error: somethign had the wrong value
# Runtime error: most other thigns
# Custom error
