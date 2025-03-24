cash = int(input("Введите число от 1 до 99: "))
if 1 <= cash <= 99:
    print(cash, end=" ")
    if (cash == 1 or cash % 10 == 1) and cash != 11:
        print("копейка")
    elif (cash == 2 or cash % 10 == 2) and cash != 12:
        print("копейки")
    elif (cash == 3 or cash % 10 == 3) and cash != 13:
        print("копейки")
    elif (cash == 4 or cash % 10 == 4) and cash != 14:
        print("копейки")
    else:
        print("копеек")
else:
    print("Ошибка: введено неверное число")
