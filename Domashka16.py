import re
# №1
# test = "28-08-2021"
input_date = input("Введите дату в формате dd-mm-YYYY:")[:10]
pattern = r"(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19[7-9]\d|20[0-2][0-5])"
res = re.findall(pattern, input_date)
print("Некорректная дата" if res == [] else res)

# №2
# test = "28-08-2021"
pattern = r"(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19[7-9]\d|20[0-2][0-5])"
while True:
    input_date = input("Введите дату в формате dd-mm-YYYY:")[:10]
    res = re.findall(pattern, input_date)
    if len(str(res)) > 2:
        print(res)
        break
    else:
        print("Некорректная дата", end="\n\n")
# №3
# test = "28-08-2021"
# pattern = r"(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19[7-9]\d|20[0-2][0-5])"
res = []


def valid_date(str_date):
    global res
    res = re.findall(r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19[7-9]\d|20[0-2][0-5])$", str_date)
    print("Некорректная дата" if res == [] else res)


input_date = input("Введите дату в формате dd-mm-YYYY:")
valid_date(input_date)

