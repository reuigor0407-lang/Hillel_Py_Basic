def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    yield begin
    count = 1
    while count < end:
        begin = func(begin)
        yield begin
        count += 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print('OK')