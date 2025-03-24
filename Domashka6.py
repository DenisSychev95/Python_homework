# Длинный вариант решения
s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
j = []
for i in s:
    if s.count(i) == 1:
        j.append(i)
for i in j:
    print(i, end=" ")

# Короткий вариант решения
s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
j = [i for i in s if s.count(i) == 1]
for i in j:
    print(i, end=" ")

# Короткий вариант решения без создания второго списка
s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in s:
    if s.count(i) == 1:
        print(i, end=" ")


