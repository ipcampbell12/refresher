

class ClassTest:

    # gets instance/object
    def instance_method(self):
        print(f"Called instance method of {self}")

    # gets class
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # doesn't get anything
    @staticmethod
    def static_method():
        print("Called static_method")


test = ClassTest()

# these two functions are two ways of doing the same thing
test.instance_method()
ClassTest.instance_method(test)

# don't need any args
ClassTest.class_method()

# won't get any anything
ClassTest.static_method()
