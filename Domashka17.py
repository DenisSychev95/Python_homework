lst = [-2, 3, 8, -11, -4, 6]


def count_numbers(my_lst):
    if len(my_lst) == 1:
        return 1 if my_lst[0] < 0 else 0
    return (1 if my_lst[0] < 0 else 0) + count_numbers(my_lst[1:])


print(f"n = {count_numbers(lst)}")



