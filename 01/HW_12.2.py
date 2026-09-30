def generate_cube_numbers(end):

    a = 2
    while a ** 3 <= end:
        yield a ** 3
        a += 1
    return a

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("OK")