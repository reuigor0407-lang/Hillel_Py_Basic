def common_elements():
    numbers_3 = list(range(0, 100, 3))
    numbers_5 = list(range(0, 100, 5))

    numbers_3 = set(numbers_3)
    numbers_5 = set(numbers_5)

    return numbers_3 & numbers_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}