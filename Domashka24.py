from math import sqrt


class Pair:
    __slots__ = ["__a", "__b"]

    def __init__(self, a: int | float, b: int | float) -> None:
        self.a = a
        self.b = b

    @staticmethod
    def check_value(value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Некорректный тип данных при вводе значения")
        if not value > 0:
            raise ValueError("Некорректное значение для ввода данных")

    @property
    def a(self) -> int | float:
        return self.__a

    @a.setter
    def a(self, new_a: int | float) -> None:
        self.check_value(new_a)
        self.__a = new_a

    @property
    def b(self) -> int | float:
        return self.__b

    @b.setter
    def b(self, new_b: int | float) -> None:
        self.check_value(new_b)
        self.__b = new_b

    def get_sum(self) -> int | float:
        return self.__a + self.__b

    def get_multy(self) -> int | float:
        return self.__a * self.__b


class RightTriangle(Pair):
    __slots__ = []
    __symbol = "\u25B3ABC"

    def __str__(self) -> str:
        return f"Прямоугольный треугольник {RightTriangle.__symbol} ({self.a}, {self.b}, {self.get_hypotenuse()})"

    def get_hypotenuse(self) -> int | float:
        return round(sqrt(self.a ** 2 + self.b ** 2), 2)

    def show_hypotenuse(self) -> None:
        print(f"Гипотенуза {RightTriangle.__symbol}: {self.get_hypotenuse()}")

    def show_sum(self) -> None:
        print(f"Сумма: {super().get_sum()}")

    def show_multy(self) -> None:
        print(f"Произведение: {super().get_multy()}")

    def get_area_triangle(self) -> int | float:
        return super().get_multy() / 2

    def show_area_triangle(self) -> None:
        print(f"Площадь {RightTriangle.__symbol}: {self.get_area_triangle()}")


rt1 = RightTriangle(5, 8)
rt1.show_hypotenuse()
print(rt1)
rt1.show_area_triangle()
print()
rt1.show_sum()
rt1.show_multy()
print()
rt1.a = 9.06
rt1.b = 9.06
rt1.show_hypotenuse()
rt1.a = 10
rt1.b = 20
rt1.show_hypotenuse()
rt1.show_sum()
rt1.show_multy()
rt1.show_area_triangle()
