# # Работа с двумя файлами
# data0 = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"
# file0 = "file_to_read.txt"
# file1 = "file_res.txt"
# with open(file0, "w+") as fwr:
#     fwr.write(data0)
#     fwr.seek(0)
#     lst0 = fwr.readlines()
#     # fwr.seek(0)
#     # print(f"{file0} создан и успешно записан. Содержимое {file0}:\n{fwr.read()}")
#
#
# def file_change_line2(my_lst, f2, p1, p2):
#     with open(f2, "w+") as fw:
#         if 0 <= p1 <= len(my_lst) - 1 and 0 <= p2 <= len(my_lst) - 1:
#             if p1 != p2:
#                 my_lst[p1], my_lst[p2] = my_lst[p2], my_lst[p1]
#                 fw.writelines(my_lst)
#                 fw.seek(0)
#                 print(f"{file1} создан,записан с учетом изменения позиции строк {file0} по условию задачи\n")
#             else:
#                 fw.writelines(my_lst)
#                 fw.seek(0)
#                 print(f"{file1} создан,записан. Позиции строк {file0} не изменены,их номера равны-({pos1},{pos2}).\n")
#         else:
#             print(f"{file1} создан и является пустым, т.к ", end="")
#             if (p1 < 0 or p1 > len(my_lst) - 1) and (p2 < 0 or p2 > len(my_lst) - 1):
#                 print(f"строк с номерами: ({pos1},{pos2}) - нет в файле {file0}.\n")
#             else:
#                 res = pos1 if (p1 < 0 or p1 > len(my_lst) - 1) else pos2
#                 print(f"строки с номером: {res} - не существует в файле {file0}.\n")
#         print(f"Результирующее содержимое {file1}:\n{fw.read()}")
#
#
# pos1 = int(input("Номер первой строки: "))
# pos2 = int(input("Номер второй строки: "))
# file_change_line2(lst0, file1, pos1, pos2)

# Работа в пределах одного файла
data = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"
file = "file_homework.txt"


def file_change_line1(my_data, f1, p1, p2):
    with open(f1, "w+") as fr:
        fr.write(my_data)
        fr.seek(0)
        print(f"\n{file} создан и успешно записан. Содержимое {file} после записи: \n{fr.read()}")
        fr.seek(0)
        lst = fr.readlines()
        fr.seek(0)
        if 0 <= p1 <= len(lst) - 1 and 0 <= p2 <= len(lst) - 1:
            if p1 != p2:
                lst[p1], lst[p2] = lst[p2], lst[p1]
                fr.writelines(lst)
                fr.seek(0)
                print("Изменение позиции строк произведено успешно.\n")
            else:
                print(f"Изменений в {file} не произведено, строки в {file} есть,но их номера равны-({pos1},{pos2})\n")
        else:
            print(f"Изменений в {file} не произведено. ", end="")
            if (p1 < 0 or p1 > len(lst) - 1) and (p2 < 0 or p2 > len(lst) - 1):
                print(f"В {file} не существует строк с номерами ({pos1},{pos2}).\n")
            else:
                res = pos1 if (p1 < 0 or p1 > len(lst) - 1) else pos2
                print(f"В {file} не существует строки с номером {res}.\n")
        print(f"Результирующее содержимое {file}:\n{fr.read()}")


pos1 = int(input("Номер первой строки:"))
pos2 = int(input("Номер второй строки:"))
file_change_line1(data, file, pos1, pos2)


