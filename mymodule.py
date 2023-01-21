import libs.mylib


def divide(dividend, divisor):
    return dividend/divisor


# __name__ is global variable in python that changes dependign on which file you are in

#__name__ = __main__
print("mymodule.py: ", __name__)
