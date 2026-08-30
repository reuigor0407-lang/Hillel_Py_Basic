my_list = []
lst = len(my_list) % 2
size = len(my_list) // 2
point = int(size + 1)

if lst == 0:
    a = my_list[:size]
    b = my_list[size:]
    new_list = [a] + [b]
    print(new_list)
else:
    a = my_list[:point]
    b = my_list[point:]
    new_list = [a] + [b]
    print(new_list)
