value = int(input())

if value > 9:
    while value > 9:
        a = 1
        while value != 0:
            a = a * (value % 10)
            value = value // 10
        value = a
    print(value)
else:
    print(value)