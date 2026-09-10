my_list = [0, 1, 7, 2, 4, 8]

if len(my_list) == 0:
    print(0)
else:
    total = 0

    for value in range(len(my_list)):
        if value % 2 == 0:
         total = total + my_list[value]

    result = total * my_list[-1]
    print(result)