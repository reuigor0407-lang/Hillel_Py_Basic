def prime_generator(end):

    for num in range(2, end + 1):
        a = 2
        res = True

        while a < num:
            if num % a == 0:
                res = False
                break
            a += 1

        if res:
            yield num

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True
assert list(prime_generator(10)) == [2, 3, 5, 7]
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print('Ok')
