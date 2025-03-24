# # Способ №1
# from math import pi, sqrt, pow
# f = int(input("Вычисление площади фигур \n\nВыбор фигуры: \n1-треугольник \n2-прямоугольник \n3-круг \n:"))
# if f == 1:
#     a = int(input("Введите сторону a= "))
#     b = int(input("Введите сторону b= "))
#     c = int(input("Введите сторону c= "))
#     lst = [a, b, c]
#     p = sum(lst) / 2
#     print("Площадь треугольника:", round(sqrt((p * (p - a) * (p - c) * (p - b))), 2))
# elif f == 2:
#     a = int(input("Введите сторону a= "))
#     b = int(input("Введите сторону b= "))
#     print("Площадь прямоугольника:", a * b)
# elif f == 3:
#     r = int(input("Введите значение радиуса r= "))
#     print("Площадь круга:", round(pi * pow(r, 2), 2))
# else:
#     print("Ошибка: введено некорректное значение по условию задачи")

# # Способ №2
# from math import pi, sqrt, pow
# print("Вычисление площади фигур", end="\n\n")
# while True:
#     f = int(input("Выбор фигуры: \n1-треугольник \n2-прямоугольник \n3-круг \n:"))
#     if f == 1:
#         lst = [int(input("Введите длину стороны:")) for e in range(3)]
#         p = sum(lst) / 2
#         print("Площадь треугольника:", round(sqrt((p * (p - lst[0]) * (p - lst[1]) * (p - lst[2]))), 2))
#         break
#     elif f == 2:
#         lst = [int(input("Введите длину стороны:")) for e in range(2)]
#         print("Площадь прямоугольника:", lst[0] * lst[1])
#         break
#     elif f == 3:
#         r = int(input("Введите значение радиуса r= "))
#         print("Площадь круга:", round(pi * pow(r, 2), 2))
#         break
#     else:
#         print("Ошибка: введено некорректное значение по условию задачи", end="\n\n")

# # Способ №3 с обработкой исключений
# from math import pi, sqrt, pow
# print("Вычисление площади фигур", end="\n\n")
# lst = []
# while True:
#     try:
#         f = int(input("Выбор фигуры: \n1-треугольник \n2-прямоугольник \n3-круг \n:"))
#         if f == 1:
#             while True:
#                 try:
#                     i = int(input("Введите длину стороны:"))
#                     if i <= 0:
#                         raise Exception("Некорректное значение")
#                     else:
#                         lst.append(i)
#                         if len(lst) == 3:
#                             break
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             p = sum(lst) / 2
#             print("Площадь треугольника:", round(sqrt((p * (p - lst[0]) * (p - lst[1]) * (p - lst[2]))), 2))
#             break
#         elif f == 2:
#             while True:
#                 try:
#                     i = int(input("Введите длину стороны:"))
#                     if i <= 0:
#                         raise Exception("Некорректное значение")
#                     else:
#                         lst.append(i)
#                         if len(lst) == 2:
#                             break
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             print("Площадь прямоугольника:", lst[0] * lst[1])
#             break
#         elif f == 3:
#             while True:
#                 try:
#                     r = int(input("Введите длину радиуса:"))
#                     if r > 0:
#                         break
#                     else:
#                         raise Exception("Некорректное значение")
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             print("Площадь круга:", round(pi * pow(r, 2), 2))
#             break
#         else:
#             print("Ошибка: введено некорректное значение по условию задачи", end="\n\n")
#     except ValueError:
#         print("Ошибка: нужно ввести число", end="\n\n")
