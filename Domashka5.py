# lst-список
# i- значение индекса списка
res = 0
lst = [int(input("->")) for i in range(int(input("n= ")))]
for i in range(len(lst)):
    if lst[i] < 0:
        res += lst[i]
print(f"Сумма отрицательных элементов: {res}")





