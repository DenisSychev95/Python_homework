# Вариант без проверок
from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @abstractmethod
    def print_info(self):
        pass

    def person_info(self):
        print(f"{self.surname} {self.name} {self.age} {self.print_info()}")


class Student(Human):
    def __init__(self, surname, name, age, study, group, average):
        super().__init__(surname, name, age)
        self.study = study
        self.group = group
        self.average = average

    def print_info(self):  # студент
        return f"{self.study} {self.group} {self.average}"


class Teacher(Human):
    def __init__(self, surname, name, age, discipline, skill):
        super().__init__(surname, name, age)
        self.discipline = discipline
        self.skill = skill

    def print_info(self):  # учитель
        return f"{self.discipline} {self.skill}"


class Graduate(Student):
    def __init__(self, surname, name, age, study, group, average, project):
        super().__init__(surname, name, age, study, group, average)
        self.project = project

    def print_info(self):  # выпускник
        return f"{super().print_info()} {self.project}"


st1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
st2 = Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5)
gr1 = Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных")
tch1 = Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110)
st3 = Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5)
tch2 = Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
lst = [st1, st2, gr1, tch1, st3, tch2]
for i in lst:
    i.person_info()

# # Вариант с проверками
# from abc import ABC, abstractmethod
# import re
#
#
# class Human(ABC):
#     __slots__ = "__surname", "__name", "__age"
#
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def check_name_surname(value):
#         if not isinstance(value, str):
#             raise TypeError("Некорректный тип данных")
#         if len(re.findall(r"^[a-zа-яё-]+$", value, re.IGNORECASE)) == 0:
#             raise ValueError("Некорректное значение")
#
#     @staticmethod
#     def check_age(age):
#         if not isinstance(age, int):
#             raise TypeError("Некорректный тип данных")
#         if age < 14:
#             raise ValueError("Некорректное значение")
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.check_name_surname(surname)
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.check_name_surname(name)
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.check_age(age)
#         self.__age = age
#
#     @abstractmethod
#     def print_info(self):
#         pass
#
#     def person_info(self):  # итоговый вывод информации
#         print(f"{self.surname} {self.name} {self.age} {self.print_info()}")
#
#
# class Student(Human):
#     __slots__ = "__study", "__group", "__average"
#
#     def __init__(self, surname, name, age, study, group, average):
#         super().__init__(surname, name, age)
#         self.study = study
#         self.group = group
#         self.average = average
#
#     @staticmethod
#     def check_study(st):
#         if not isinstance(st, str):
#             raise TypeError("Некорректный тип данных")
#         if len(re.findall(r"^[a-zа-яё-]+$", st, re.IGNORECASE)) == 0:
#             raise ValueError("Некорректное значение")
#
#     @staticmethod
#     def check_group(gr):
#         if not isinstance(gr, str):
#             raise TypeError("Некорректный тип данных")
#         if len(re.findall(r"^[a-zа-яё_-]+\d{3,}$", gr, re.IGNORECASE)) == 0:
#             raise ValueError("Некорректное значение")
#
#     @staticmethod
#     def check_average(av):
#         if not isinstance(av, int):
#             raise TypeError("Некорректный тип данных")
#         if not 2 <= av <= 5:
#             raise ValueError("Некорректное значение")
#
#     @property
#     def study(self):
#         return self.__study
#
#     @study.setter
#     def study(self, study):
#         self.check_study(study)
#         self.__study = study
#
#     @property
#     def group(self):
#         return self.__group
#
#     @group.setter
#     def group(self, group):
#         self.check_group(group)
#         self.__group = group
#
#     @property
#     def average(self):
#         return self.__average
#
#     @average.setter
#     def average(self, average):
#         self.check_average(average)
#         self.__average = average
#
#     def print_info(self):  # студент
#         return f"{self.study} {self.group} {self.average}"
#
#
# class Teacher(Human):
#     __slots__ = "__discipline", "__skill"
#
#     def __init__(self, surname, name, age, discipline, skill):
#         super().__init__(surname, name, age)
#         self.discipline = discipline
#         self.skill = skill
#
#     @staticmethod
#     def check_discipline(disc):
#         if not isinstance(disc, str):
#             raise TypeError("Некорректный тип данных")
#         if len(re.findall(r"^[a-zа-яё\s-]+$", disc, re.IGNORECASE)) == 0:
#             raise ValueError("Некорректное значение")
#
#     @staticmethod
#     def check_skill(skill):
#         if not isinstance(skill, int):
#             raise TypeError("Некорректный тип данных")
#         if skill < 10:
#             raise ValueError("Некорректное значение")
#
#     @property
#     def discipline(self):
#         return self.__discipline
#
#     @discipline.setter
#     def discipline(self, discipline):
#         self.check_discipline(discipline)
#         self.__discipline = discipline
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, skill):
#         self.__skill = skill
#
#     def print_info(self):  # учитель
#         return f"{self.discipline} {self.skill}"
#
#
# class Graduate(Student):
#     __slots__ = "__project",
#
#     def __init__(self, surname, name, age, study, group, average, project):
#         super().__init__(surname, name, age, study, group, average)
#         self.project = project
#
#     @staticmethod
#     def check_project(pr):
#         if not isinstance(pr, str):
#             raise TypeError("Некорректный тип данных")
#         lst_ = pr.split()
#         for e in lst_:
#             if len(re.findall(r"^[a-zа-яё]+$", e, re.IGNORECASE)) == 0:
#                 raise ValueError("Некорректное значение")
#
#     @property
#     def project(self):
#         return self.__project
#
#     @project.setter
#     def project(self, project):
#         self.check_project(project)
#         self.__project = project
#
#     def print_info(self):  # выпускник
#         return f"{super().print_info()} {self.project}"
#
#
# st1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
# st2 = Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5)
# gr1 = Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных")
# tch1 = Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110)
# st3 = Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5)
# tch2 = Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# lst = [st1, st2, gr1, tch1, st3, tch2]
# for i in lst:
#     i.person_info()
