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

    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.matter1, reverse=True)
        print("\nClassement matière 1 :")
        for s in sorted_students:
            print(s.name, s.matter1)

if __name__ == "__main__":
    school_class = SchoolClass()

    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    school_class.rank_matter_1()

    print("Étudiants ajoutés :")
    for s in school_class.students:
        print(s.name, s.matter1, s.matter2, s.matter3)