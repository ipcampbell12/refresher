

class ClassTest:

    # gets instance/object
    # all functions inside a class that use the object as first parameter are called instance methods
    # called on class instance (same thing as an object)
    # used for most things
    # produce an action that acts upon data inside the object
    def instance_method(self):
        print(f"Called instance method of {self}")

    # gets class
    # a reference to the class itself
    # doens't require an instance(object) to be run
    # cls refers to the class itself
    # usually used as a factory
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # doesn't get anything
    # no parameter of cls or self
    # don't get class or instance
    # just a function that lives inside the class, no information about class or object
    # makes sense for code organization
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
