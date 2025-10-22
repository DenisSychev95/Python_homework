from django.shortcuts import render
from django.http import HttpResponse
import random


# def home(request):
#     return HttpResponse("Hello")


def home(request):
    lst = list(range(6, 15))
    return render(request, "generator/home.html", {"lst": lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])
        char.extend([chr(i) for i in range(58, 65)])
        char.extend([chr(i) for i in range(91, 97)])
        char.extend([chr(i) for i in range(123, 127)])

    print(char)
    length = int(request.GET.get('length'))
    psw = ""
    for i in range(length + 1):
        psw += random.choice(char)
    return render(request, "generator/password.html", {"password": psw})


def about(request):
    tags = ["Установить длину пароля", "Добавить/убрать заглавные буквы", "Добавить/убрать цифры",
            "Добавить/убрать спецсимволы"]
    return render(request, "generator/about.html", {"title": "Вас приветствует генератор паролей!",
                                                    "button": "На главную", "tags": tags})
