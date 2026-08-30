my_list = [5, 45, "rr", 55, 48, "frd"]
size = len(my_list)
if size == 0:
    print(my_list)
else:
    a = [my_list[-1]]
    b = my_list[:-1]
    a.extend(b)
    print(a)
    print()

    x = [my_list.pop(-1)]
    x.extend(my_list)
    print(x)


