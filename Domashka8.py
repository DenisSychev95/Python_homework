# #_____________________Способ №1 без обработки исключений___________________________
# from math import pi, pow
# f = int(input("Вычисление площади фигур \n\nВыбор фигуры:\n1 - прямоугольник\n2 - треугольник\n3 - круг \n:"))
# if f == 1:  # прямоугольник
#     def s_rectangle(a, b):
#         return a * b
#
#
#     lst = [(int(input("Введите длину стороны:"))) for i in range(2)]
#     print(f"Площадь: {s_rectangle(lst[0], lst[1]):.2f}")
# elif f == 2:  # треугольник
#     def s_triangle(a, h):
#         return (a * h) / 2
#
#
#     num_1 = int(input("Основание: "))
#     num_2 = int(input("Высота: "))
#     print(f"Площадь: {s_triangle(num_1, num_2):.2f}")
# elif f == 3:  # круг
#     def s_circle(r):
#         return pow(r, 2) * pi
#
#
#     rad = int(input("Радиус: "))
#     print(f"Площадь: {s_circle(rad):.2f}")
# else:
#     print("Ошибка: введено некорректное значение по условию задачи")

# #___________________Способ №2 с обработкой исключений__________________________________
# from math import pi, pow
# lst = []
# print("Вычисление площади фигур", end="\n\n")
# while True:
#     try:  # Проверка корректности ввода условия задачи
#         f = int(input("Выбор фигуры:\n1 - прямоугольник\n2 - треугольник\n3 - круг \n:"))
#         if f == 1:  # Прямоугольник
#             def s_rectangle(a, b):
#                 return a * b
#
#
#             while True:
#                 try:
#                     i = int(input("Введите длину стороны:"))
#                     if i > 0:
#                         lst.append(i)
#                         if len(lst) == 2:
#                             break
#                     else:
#                         raise Exception("Некорректное значение")
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             print(f"Площадь: {s_rectangle(lst[0], lst[1]):.2f}")
#             break
#
#         elif f == 2:  # Треугольник
#             def s_triangle(a, h):
#                 return (a * h) / 2
#
#
#             while True:
#                 try:
#                     num_1 = int(input("Основание: "))
#                     if num_1 > 0:
#                         break
#                     else:
#                         raise Exception("Некорректное значение")
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             while True:
#                 try:
#                     num_2 = int(input("Высота: "))
#                     if num_2 > 0:
#                         break
#                     else:
#                         raise Exception("Некорректное значение")
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             print(f"Площадь: {s_triangle(num_1, num_2):.2f}")
#             break
#         elif f == 3:  # Круг
#             def s_circle(r):
#                 return pow(r, 2) * pi
#
#
#             while True:
#                 try:
#                     rad = int(input("Введите длину радиуса:"))
#                     if rad > 0:
#                         break
#                     else:
#                         raise Exception("Некорректное значение")
#                 except ValueError:
#                     print("Ошибка: нужно ввести число", end="\n\n")
#                 except Exception as e:
#                     print(e, end="\n\n")
#             print(f"Площадь: {s_circle(rad):.2f}")
#             break
#         else:
#             print("Ошибка: введено некорректное значение по условию задачи")
#     except ValueError:
#         print("Ошибка: нужно ввести число", end="\n\n")


