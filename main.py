from collections.abc import Iterable, Iterator

def add_matter4(cls):
    original_init = cls.__init__

    def new_init(self, name, matter1, matter2, matter3):
        original_init(self, name, matter1, matter2, matter3)
        self.matter4 = 0

    cls.__init__ = new_init
    return cls

@add_matter4
class Student:
    def __init__(self, name, matter1, matter2, matter3):
        self.name = name
        self.matter1 = matter1
        self.matter2 = matter2
        self.matter3 = matter3

    def average(self):
        return (self.matter1 + self.matter2 + self.matter3) / 3

class Matter1Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter1, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student

class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student

class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter3, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student

class Matter4Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter4, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student

def add_iterator_matter4(cls):
    def get_matter4_iterator(self):
        return Matter4Iterator(self.students)

    cls.get_matter4_iterator = get_matter4_iterator
    return cls
       
@add_iterator_matter4
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
            cls._instance.students = []
        return cls._instance

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.matter1, reverse=True)
        print("\nClassement matière 1 :")
        for s in sorted_students:
            print(s.name, s.matter1)

    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.matter2, reverse=True)
        print("\nClassement matière 2 :")
        for s in sorted_students:
            print(s.name, s.matter2)

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.matter3, reverse=True)
        print("\nClassement matière 3 :")
        for s in sorted_students:
            print(s.name, s.matter3)

    def __iter__(self):
        return Matter1Iterator(self.students)

if __name__ == "__main__":
    school_class = SchoolClass()

    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("Étudiants ajoutés")
    for s in school_class.students:
        print(s.name, s.matter1, s.matter2, s.matter3)

    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    print("\nIterator matière 1")
    for s in school_class:
        print(s.name, s.matter1)

    print("\nIterator matière 2")
    for s in Matter2Iterator(school_class.students):
        print(s.name, s.matter2)

    print("\nIterator matière 3")
    for s in Matter3Iterator(school_class.students):
        print(s.name, s.matter3)

    print("\nMatière 4")
    for s in school_class.students:
        print(s.name, s.matter4)

    print("\nIterator matière 4")
    for s in school_class.get_matter4_iterator():
        print(s.name, s.matter4)

    print("\nTest Singleton")
    sc1 = SchoolClass()
    sc2 = SchoolClass()

    print(sc1 is sc2)