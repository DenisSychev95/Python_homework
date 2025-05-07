if __name__ == "__main__":
    import requests

    # С вашего позволения я создам на вашем компьютере 2 модуля и импортирую их в этот документ, спасибо!

    # Создаем и импортируем модуль my_first_custom_module.py для работы с экземплярами класса Country
    module_name1 = "my_first_custom_module.py"
    response1 = requests.get(
        "https://raw.githubusercontent.com/DenisSychev95/Python_homework/refs/heads/master/custom_module_.py")
    response_str1 = response1.text
    with open(module_name1, "w", encoding="utf-8") as fw:
        fw.write(response_str1)

    # Создаем и импортируем модуль my_second_custom_module.py для работы с классом CountryStatic
    module_name2 = "my_second_custom_module.py"
    response2 = requests.get(
        "https://raw.githubusercontent.com/DenisSychev95/Python_homework/refs/heads/master/custom_module_static.py")
    response_str2 = response2.text
    with open(module_name2, "w", encoding="utf-8") as fw:
        fw.write(response_str2)

    # # Вся реализация домашнего задания упакована в созданные и импортированные выше модули.
    # # Пожалуйста, раскомментируйте и запустите, спасибо!
    # # Вариант №1 более сложный и интересный через экземпляры класса Country
    # from my_first_custom_module import Country
    #
    # # valid_data1 = {"Беларусь": "Минск"}
    # # valid_data2 = [["Japan", "Tokio"]]
    # # valid_data3 = [("Great Britain", "London")]
    # # valid_data4 = (("Египет", "Каир"),)
    # # valid_filename = "data_filename"
    # c1 = Country()
    # print(c1.__dict__)
    # # # c1()
    #
    # # Вариант №2 более простой: работа со статическими методами класса CountryStatic
    # from my_second_custom_module import CountryStatic
    # # # CountryStatic.cycle()
    