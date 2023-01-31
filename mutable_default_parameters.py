from typing import List, Optional


# shouldn't make a parameter equal to a mutable value by default
# function parameters evalue when function is defined, not when function is called

class Student:
    def __init__(self, name: str, grades: List[int] = []):  # this is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

# rolf with have a 90 even though he hasn't taken any exams
# grades for both students are actually names for the same list
# if you the same default parameter for all your students, they will end up sharing grades


# better approach
class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


# could also import Optional from typing and make it an optional list of integers

class Student:
    # this is bad!
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)

# should not use default parameter values that are mutable
