# WITHOUT oop
student_dict = {"name": "Jim", "grades": (45, 67, 89, 13)}

# this function doesn't know anything about the student


def average(sequence):
    return sum(sequence)/len(sequence)


# print(average(student_dict["grades"]))


# WITH oop - the function WILL know about the grades
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)


# call a class, init method runs, create object
student = Student("Bob", (80, 67, 95, 13))
student2 = Student("James", (2, 67, 95, 13))

print(student.name)
print(student.grades)

# create a new object from class, can call the method
# pass object instance to class method
print(Student.average(student))


# but you can call the method on the object itself
print(student.average())
print(student2.average())
