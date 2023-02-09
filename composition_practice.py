class ClassRoom:
    def __init__(self, id, teacher, subject, *students):
        self.id = id
        self.students = students
        self.teacher = teacher
        self.subject = subject

    def __str__(self):
        return f"Professor {self.teacher} teaches {self.subject} and currently has {len(self.students)} students: {','.join(str(x) for x in self.students)}"


class Person:
    def __init__(self, id, first_name, last_name, role):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Teacher(Person):
    def __init__(self, id, first_name, last_name, role, salary):
        super().__init__(id, first_name, last_name, role)
        self.salary = salary


class Student(Person):
    def __init__(self, id, first_name, last_name, role, grades):
        super().__init__(id, first_name, last_name, role)
        self.grades = grades


teacher1 = Teacher(1, 'Minerva', "McGonagall", "Teacher", 25000)
student1 = Student(1, "Harry", "Potter", "Student", [75, 87, 71])
student2 = Student(2, "Ronald", "Weasley", "Student", [32, 43, 58])
student3 = Student(2, "Hermione", "Granger", "Student", [95, 97, 100])
class1 = ClassRoom(1, teacher1, "Transfiguration",
                   student1, student2, student3)

print(class1)
print(student3)
