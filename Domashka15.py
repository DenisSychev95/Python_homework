# s_test = "I am learning Python. hello, WORLD!"

# Через конкатенацию
s = input("Введите строку: ")
h0 = s.find("h")
h1 = s.rfind("h")
print(s[:h0] + s[h0:h1 + 1][::-1] + s[h1+1:])

# Через метод replace
s = input("Введите строку: ")
h0 = s.find("h")
h1 = s.rfind("h")
print(s.replace(s[h0:h1 + 1], s[h0:h1 + 1][::-1]))

# Самый короткий способ
s = input("Введите строку: ")
print(s.replace(s[s.find("h"):s.rfind("h") + 1], s[s.find("h"):s.rfind("h") + 1][::-1]))

