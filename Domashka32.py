import os
import os.path
import requests

directory = "sychev_pocket"
if not os.path.exists(directory):
    os.mkdir(directory)

path_directory = os.path.join(os.getcwd(), directory)
file_name1 = os.path.join(path_directory, "__init__.py")
file_name2 = os.path.join(path_directory, "f_model.py")
file_name3 = os.path.join(path_directory, "f_controller.py")
file_name4 = os.path.join(path_directory, "f_view.py")
response1 = requests.get(
    "https://raw.githubusercontent.com/DenisSychev95/Python_homework/refs/heads/master/f_model.py").text
response2 = requests.get(
    "https://raw.githubusercontent.com/DenisSychev95/Python_homework/refs/heads/master/f_controller.py").text
response3 = requests.get(
    "https://raw.githubusercontent.com/DenisSychev95/Python_homework/refs/heads/master/f_view.py").text

with open(file_name1, "w", encoding="utf-8") as f:
    f.write("")
with open(file_name2, "w", encoding="utf-8") as f:
    f.write(response1)
with open(file_name3, "w", encoding="utf-8") as f:
    f.write(response2)
with open(file_name4, "w", encoding="utf-8") as f:
    f.write(response3)

# Ссылка на файл с 20-ю заполненными фильмами
file_path = "https://github.com/DenisSychev95/Python_homework/blob/master/films.txt"

# # Пожалуйста, запустите этот блок кода повторно для тестирования приложения
# from sychev_pocket.f_controller import Controller
#
#
# def project():
#     project_hw = Controller()
#     project_hw.start()
#
#
# if __name__ == "__main__":
#     project()
