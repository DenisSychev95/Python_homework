master_dict = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}
while True:
    name = input("Имя: ")
    if name in master_dict.keys():
        while True:
            reg = input("Регион: ")
            if reg in master_dict[name].keys():
                sales = master_dict[name][reg]
                print("Текущий объем продаж: ", sales)
                while True:
                    try:
                        new_sales = int(input("Новое значение:"))
                        if new_sales >= 0:
                            master_dict[name][reg] = new_sales
                            print(master_dict[name])
                            break
                        else:
                            raise Exception("Некорректное значение объема продаж")
                    except ValueError:
                        print("Введите объем продаж числовым значением")
                    except Exception as e:
                        print(e)
                break
            else:
                print("Некорректное значение региона")
        break
    else:
        print("Некорректное имя сотрудника")
