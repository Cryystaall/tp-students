class Student:
    def __init__(self, name, matter1, matter2, matter3):
        self.name = name
        self.matter1 = matter1
        self.matter2 = matter2
        self.matter3 = matter3

    def average(self):
        return (self.matter1 + self.matter2 + self.matter3) / 3


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
