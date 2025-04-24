from abc import ABC, abstractmethod
from math import sqrt


# Декорирующая функция для метода print_info
def my_topping(name, lenght):
    def decorator(func):
        def inner(*args, **kwargs):
            print(name.center(lenght, "="))
            func(*args, **kwargs)
        return inner
    return decorator

# # Декорирующий класс для метода print_info
# class MyTopping:
#     def __init__(self, name, lenght):
#         self.name = name
#         self.lenght = lenght
#
#     def __call__(self, func):
#         def inner(*args, **kwargs):
#             print(self.name.center(self.lenght, "="))
#             func(*args, **kwargs)
#         return inner


class Shape(ABC):
    def __init__(self, color, a=None, b=None, c=None):
        if b and c is None:
            self.a = a
            self.color = color
        if c is None:
            self.a = a
            self.b = b
            self.color = color
        else:
            self.a = a
            self.b = b
            self.c = c
            self.color = color

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def draw_shape(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def get_color(self):
        pass


class Square(Shape):
    def __str__(self):
        return f"Сторона: {self.a}"

    def perimetr(self):
        print(f"Периметр: {self.a * 4}")
        return self.a * 4

    def square(self):
        print(f"Площадь: {self.a ** 2}")
        return self.a ** 2

    def draw_shape(self):
        pattern = (("*" * 3).center(17) + "\n") * 3
        print(pattern)
        return pattern

    def get_color(self):
        print(f"Цвет: {self.color}")
        return f"Цвет: {self.color}"

    @my_topping("Квадрат", 13)
    # @MyTopping("Квадрат", 13)
    def print_info(self):
        print(self)
        self.get_color()
        self.square()
        self.perimetr()
        self.draw_shape()


class Rectangle(Shape):
    def __str__(self):
        return f"Длина: {self.a}\nШирина: {self.b}"

    def perimetr(self):
        print(f"Периметр: {(self.a + self.b) * 2}")
        return (self.a + self.b) * 2

    def square(self):
        print(f"Площадь: {self.a * self.b}")
        return self.a * self.b

    def draw_shape(self):
        pattern = (("*" * 8).center(15) + "\n") * 3
        print(pattern)
        return pattern

    def get_color(self):
        print(f"Цвет: {self.color}")
        return f"Цвет: {self.color}"

    @my_topping("Прямоугольник", 19)
    # @MyTopping("Прямоугольник", 19)
    def print_info(self):
        print(self)
        self.get_color()
        self.square()
        self.perimetr()
        self.draw_shape()


class Triangle(Shape):
    def __str__(self):
        return f"Сторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}"

    def perimetr(self):
        print(f"Периметр: {self.a + self.b + self.c}")
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        sq = round(sqrt(p * (p-self.a) * (p-self.b) * (p-self.c)), 2)
        print(f"Площадь: {sq}")
        return sq

    def draw_shape(self):
        e = 1
        pattern = ""
        for i in range(6):
            change = f"{("*" * e)}".center(13) + "\n"
            pattern += change
            e += 2
        print(pattern)
        return pattern

    def get_color(self):
        print(f"Цвет: {self.color}")
        return f"Цвет: {self.color}"

    @my_topping("Треугольник", 17)
    # @MyTopping("Треугольник", 17)
    def print_info(self):
        print(self)
        self.get_color()
        self.square()
        self.perimetr()
        self.draw_shape()


s = Square("red", 3)
r = Rectangle("green", 3, 7)
t = Triangle("yellow", 11, 6, 6)

s.print_info()
r.print_info()
t.print_info()