class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # allows you to print object info as string
    def __str__(self):
        return f"My name is {self.name}. I am {self.age} years old."

    #used in flask
    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"


# create person object instance
bob = Person("Bob", 35)

# print's string representing bob object
print(bob)
