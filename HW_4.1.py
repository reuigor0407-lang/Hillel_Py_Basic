my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

result = []

for value in my_list:
    if value != 0:
        result.append(value)

for value in my_list:
    if value == 0:
        result.append(value)

my_list = result
print(result)
