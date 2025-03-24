# Без обработки исключений
from math import ceil
count = int(input("Укажите количество студентов: "))
students = {input(f"{i+1}-й студент: "): int(input("Балл: ")) for i in range(count)}
res = ceil(sum(students.values()) / count)
print("Средний балл: ", res, ". ", "Студенты с баллом выше среднего:", sep="")
for k, v in students.items():
    if v > res:
        print(k)

# # С обработкой исключений
# from math import ceil
# lst1 = []
# lst2 = []
# i = 1
# while True:
#     try:
#         count = int(input("Укажите количество студентов: "))
#         if count > 0:
#             break
#         else:
#             raise Exception("Некорректное значение количества студентов")
#     except ValueError:
#         print("Укажите количество студентов числом")
#     except Exception as e:
#         print(e)
# while True:
#     name = input(f"{i}-й студент: ")
#     i += 1
#     lst1.append(name)
#     while True:
#         try:
#             value = int(input("Балл: "))
#             if value > 0:
#                 lst2.append(value)
#                 break
#             else:
#                 raise Exception("Некорректное значение баллов")
#         except ValueError:
#             print("Введите значение баллов числом")
#         except Exception as e:
#             print(e)
#     if len(lst2) == count:
#         break
# students = {k: v for k, v in zip(lst1, lst2)}
# res = ceil(sum(students.values()) / count)
# print("Средний балл: ", res, ". ", "Студенты с баллом выше среднего:", sep="")
# for k, v in students.items():
#     if v > res:
#         print(k)
