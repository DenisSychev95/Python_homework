# Решение через функции
import os
my_dirs = [r"work\f1", r"work\f1\f11", r"work\f2", r"work\f2\f21"]
files = {
    "work": ["w.txt", "w_empty.txt"],
    r"work\f1": ["f10.txt", "f11.txt", "f12.txt"],
    r"work\f1\f11": ["run.txt", "default.txt"],
    r"work\f2": ["hello.txt"],
    r"work\f2\f21": ["f210.txt", "f211.txt", "f212.txt"]
}
texted_files = [r"work\w.txt", r"work\F1\f12.txt", r"work\F2\F21\f211.txt", r"work\F2\F21\f212.txt"]
root_dir = "work"
empty_files_dir = r"work\empty_files"


def creator(lst_dirs, dict_files):
    """
    Создает вложенные директории, создает в указанных директориях пустые файлы

    Создает вложенные директории по принимаемому списку директорий, создает в указанных директориях
    пустые файлы по условиям принимаемого словаря ключ-директория, значение-список файлов.
    :param lst_dirs: Список создаваемых директорий
    :param dict_files: Словарь-инструкция создания файлов
    """
    for d in lst_dirs:
        if not os.path.exists(d):
            os.makedirs(d)
    for dir_w, f_w in dict_files.items():
        for file_create in f_w:
            file_path = os.path.join(dir_w, file_create)
            open(file_path, "w").close()
    print("Вложенные директории созданы, пустые файлы созданы.", end="\n\n")


def file_writer(lst_files):
    """
    Записывает в файлы что-то на ваше усмотрение.

    Записывает в каждый файл из принимаемого списка относительных путей файлов символы по усмотрению пользователя.
    :param lst_files: Список, содержащий относительные пути файлов для записи
    """
    for file_wr in lst_files:
        with open(file_wr, "w") as fw:
            fw.write(input("Скопируйте из test_text какой-то текст и сделайте вставку-->>"))
    print("\nВыбранные файлы записаны.", end="\n\n")


def stage1(m_dir):
    """
    Выводит имена и размер непустых файлов.

    Выводит относительный путь, имя и размер всех непустых файлов по принимаемому имени корневой директории.
    :param m_dir: Корневая директория по условию задания.
    """
    print("Записанные файлы и их размер:")
    for root_func, dirs_func, files_func in os.walk(m_dir):
        for file_check in files_func:
            path = os.path.join(root_func, file_check)
            size_file = os.path.getsize(path)
            if size_file > 0:
                print(f"\t{path} - {size_file} bytes")


def stage2(m_dir, m_dir2):
    """
    Создает директорию и перемещает в нее все пустые файлы из корневой директории.

    Создает директорию и перемещает в нее все пустые файлы из корневой директории, для каждого перемещаемого файла
    выводится сообщение содержащее имя файла, его старый путь относительно корневой директории и новый путь к файлу
    после перемещения в созданную директорию.
    :param m_dir: Корневая директория по условию задания.
    :param m_dir2: Директория для пустых файлов.
    """
    print("\nПеремещенные файлы и их пути:")
    for root_func2, dirs_func2, files_func2 in os.walk(m_dir):
        for file_check in files_func2:
            old_path = os.path.join(root_func2, file_check)
            new_path = os.path.join(m_dir2, file_check)
            size_file = os.path.getsize(old_path)
            if size_file == 0:
                print(f"\tФайл: {file_check}; старый путь:{old_path}; новый путь:{new_path}")
                if not os.path.exists(new_path):
                    os.renames(old_path, new_path)


def cleaner(m_dir2):
    """
    Удаляет файлы из указанной директории

    Удаляет все файлы из указанной директории, позволяет повторно запускать функцию stage1 и stage2
    :param m_dir2: Очищаемая директория
    """
    dir_empty_lst = os.listdir(m_dir2)
    print(f"\nДиректория {m_dir2}\nСписок пустых файлов: \n\t{dir_empty_lst}", end="\n\n")
    for del_file in dir_empty_lst:
        path_empty = os.path.join(empty_files_dir, del_file)
        os.remove(path_empty)
    print(f"Директория {m_dir2} очищена")


def deleter(m_dir):
    """
    Удаляет корневую директорию.

    Проверяет наличие корневой директории, удаляет все вложенные файлы, папки и саму директорию.
    :param m_dir: Удаляемая директория
    """
    if os.path.exists(m_dir):
        for root_n, dirs_n, files_n in os.walk(m_dir):
            for file_del1 in files_n:
                to_del_file = os.path.join(root_n, file_del1)
                os.remove(to_del_file)
        print(f"Все файлы корневой директории {m_dir} удалены")
        for root_n, dirs_n, files_n in os.walk(m_dir, topdown=False):
            if not os.listdir(root_n):
                os.rmdir(root_n)
        print(f"Вложенные директории {m_dir} удалены. Корневая директория удалена")


test_text = """"Компания CD Projekt RED официально подтвердила, что The Witcher 4 (рабочее название Polaris) не выйдет
до 2027 года.В рамках финансового отчёта представители студии заявили, что активная разработка началась
в конце 2024-го, а значит, ждать релиза раньше конца 2026 года не стоит.Финансовый директор Пётр Нелюбович подчеркнул,
что студия не объявляет точные сроки, но инвесторам важно понимать, что игра не успеет выйти до завершения первой фазы
программы поощрений CDPR, которая заканчивается 31 декабря 2026 года.
"""
creator(my_dirs, files)
file_writer(texted_files)
stage1(root_dir)
stage2(root_dir, empty_files_dir)
# cleaner(empty_files_dir)
# deleter(root_dir)

# Решение без функций
# import os
#
# my_dirs = [r"work\f1", r"work\f1\f11", r"work\f2", r"work\f2\f21"]  # список директорий
# for d in my_dirs:
#     if not os.path.exists(d):
#         os.makedirs(d)
# files = {
#     "work": ["w.txt", "w_empty.txt"],
#     r"work\f1": ["f10.txt", "f11.txt", "f12.txt"],
#     r"work\f1\f11": ["run.txt", "default.txt"],
#     r"work\f2": ["hello.txt"],
#     r"work\f2\f21": ["f210.txt", "f211.txt", "f212.txt"]
# }  # словарь ключ-директория, значение-список файлов директории
# for dir_, f_ in files.items():
#     for file in f_:
#         file_path = os.path.join(dir_, file)
#         open(file_path, "w").close()
# test_text = """"Компания CD Projekt RED официально подтвердила, что The Witcher 4 (рабочее название Polaris) не выйдет
# до 2027 года.В рамках финансового отчёта представители студии заявили, что активная разработка началась
# в конце 2024-го, а значит, ждать релиза раньше конца 2026 года не стоит.Финансовый директор Пётр Нелюбович подчеркнул,
# что студия не объявляет точные сроки, но инвесторам важно понимать, что игра не успеет выйти до завершения первой фазы
# программы поощрений CDPR, которая заканчивается 31 декабря 2026 года.
# """  # строка для удобства записи файлов разной длины
# texted_files = [r"work\w.txt", r"work\F1\f12.txt", r"work\F2\F21\f211.txt", r"work\F2\F21\f212.txt"]  # не пуст. файлы
# root_dir = "work"  # корневая директория задания
# empty_files_dir = r"work\empty_files"  # директория для пустых файлов по заданию
#
# for file in texted_files:
#     with open(file, "w") as fw:
#         fw.write(input("Скопируйте из test_text какой-то текст и сделайте вставку-->>"))
#
# for root, dirs, files in os.walk(root_dir):  # line 166- 171 1-й блок задания
#     for file in files:
#         path = os.path.join(root, file)
#         size_file = (os.path.getsize(path))
#         if size_file > 0:
#             print(f"{path} - {size_file} bytes")
# print()
# for root, dirs, files in os.walk(root_dir):  # line 173- 181 2-й блок задания
#     for file in files:
#         old_path = os.path.join(root, file)
#         new_path = os.path.join(empty_files_dir, file)
#         size_file = os.path.getsize(old_path)
#         if size_file == 0:
#             print(f"Файл: {file}; старый путь:{old_path}; новый путь:{new_path}")
#             if not os.path.exists(new_path):
#                 os.renames(old_path, new_path)
# # print()
# # dir_empty_lst = os.listdir(empty_files_dir)  # line 183- 188- очистка дир. с пустыми файлами для перезаписи кода
# # print(f"Директория {empty_files_dir}\nСписок пустых файлов: {dir_empty_lst}", end="\n\n")
# # for e_file in dir_empty_lst:
# #     path_empty = os.path.join(empty_files_dir, e_file)
# #     os.remove(path_empty)
# # print(f"Директория {empty_files_dir} очищена")


