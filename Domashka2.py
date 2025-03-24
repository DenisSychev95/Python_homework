# Способ №1: без использования переменных a, b, c, d, e
# вводим num (str), переводим в (int)
# получаем multiplication = 1 * 3 * 5 * 7 * 9 = 945
# получаем summa = 1 + 3 + 5 + 7 + 9 = 25
# получаем arithmetic_mean = 25 / 5 = 5.0
# print "Произведение цифр числа 97531:", multiplication, перед multiplication 1 пробел, след print на новой строке
# print "Среднее арифметическое:", arithmetic_mean, перед arithmetic_mean 2 пробела

num = int(input("Введите пятизначное число: "))
multiplication = (num % 10) * (num // 10 % 10) * (num // 100 % 10) * (num // 1000 % 10) * (num // 10000 % 10)
summa = (num % 10) + (num // 10 % 10) + (num // 100 % 10) + (num // 1000 % 10) + (num // 10000 % 10)
arithmetic_mean = summa / 5
print("Произведение цифр числа 97531:", multiplication, sep=" ", end="\n")
print("Среднее арифметическое:", arithmetic_mean, sep="  ")

# Способ №2: с использованием переменных a, b, c, d, e
# вводим num (str), переводим в (int)
# получаем а = num % 10 = 1
# получаем новую num = num // 10 = 9753
# получаем b = num % 10 = 3
# получаем новую num = num // 10 = 975
# получаем c = num % 10 = 5
# получаем новую num = num // 10 = 97
# получаем d = num % 10 = 7
# получаем новую num = num // 10 = 9
# получаем e = num % 10 = 9
# получаем multiplication = a * b * c * d * e = 945
# получаем summa = a + b + c + d + e = 25
# получаем arithmetic_mean = (a + b + c + d + e) / 5 = 5.0
# print "Произведение цифр числа 97531:", multiplication, перед multiplication 1 пробел, след print на новой строке
# print "Среднее арифметическое:", arithmetic_mean, перед arithmetic_mean 2 пробела

num = int(input("Введите пятизначное число: "))
a = num % 10
num = num // 10
b = num % 10
num //= 10
c = num % 10
num //= 10
d = num % 10
num //= 10
e = num % 10
multiplication = a * b * c * d * e
summa = a + b + c + d + e
arithmetic_mean = summa / 5
print("Произведение цифр числа 97531:", multiplication, sep=" ", end="\n")
print("Среднее арифметическое:", arithmetic_mean, sep="  ")

