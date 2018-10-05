from abc import *


class SchoolMember(metaclass=ABCMeta):
    """
        Представляет собой любого человека в школе.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Создан член школы: {}".format(self.name))

    @abstractmethod
    def tell(self):
        print("Имя: {}, возраст {}".format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Создан учитель: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Зарплата: {}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Создан ученик: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Оценки: '{0:d}'".format(self.marks))


t = Teacher("Brehov", 70, 60000)
s = Student("Vlad", 20, 75)

members = [t, s]
for i in members:
    i.tell()

