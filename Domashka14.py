def my_decorator(fn):
    def inner(*args1):
        fn(*args1)
        print("Среднее арифметическое чисел", ",".join(map(str, args1)), "=", sum(args1)/len(args1))
    return inner


@my_decorator
def summa(*args):
    print("Сумма чисел", ",".join(map(str, args)), "=", sum(args))


summa(2, 3, 3, 4)


