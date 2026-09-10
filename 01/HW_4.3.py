import random

count = random.randint(3, 10)

numbers = []
for i in range(count):
    numbers.append(random.randint(1, 10))
print(numbers)

my_list = [numbers[0], numbers[2], numbers[-2]]
print(my_list)