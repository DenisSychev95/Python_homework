# # РЕШИТЬ ЗАДАЧУ ТРЕМЯ СПОСОБАМИ!!
# №1
def rect_piped(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))  # s-local
    return s  # s-local


print(rect_piped(2, 4, 6))
print(rect_piped(5, 8, 2))
print(rect_piped(1, 6, 8))
print()
#  №2
s1 = None  # s1-global


def rect_piped1(a, b, c):
    global s1  # s1-local-> s1-global

    def inner(i, j):
        return i * j

    s1 = 2 * (inner(a, b) + inner(a, c) + inner(b, c))  # s1-local
    return s1  # s1-global


print(rect_piped1(2, 4, 6))
print(rect_piped1(5, 8, 2))
print(rect_piped1(1, 6, 8))
print()


# №3
def rect_piped2(a, b, c):
    s2 = 0

    def inner0():
        nonlocal s2  # s2-local-> s2-nonlocal

        def inner1(i, j):
            return i * j

        lst = [inner1(a, b), inner1(a, c), inner1(b, c)]
        s2 = 2 * sum(lst)  # s2-local
        return s2  # s2-nonlocal

    inner0()
    return s2  # s2-nonlocal


print(rect_piped2(2, 4, 6))
print(rect_piped2(5, 8, 2))
print(rect_piped2(1, 6, 8))

