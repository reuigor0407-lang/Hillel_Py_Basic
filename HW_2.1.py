# square_of_number
number = int(input("Enter a number: "))
print("Square of a number:", number ** 2)
print()

# arithmetic_mean
print("Enter three numbers:")
number1 = int(input("1."))
number2 = int(input("2."))
number3 = int(input("3."))
print("Arithmetic mean of three numbers:", (number1 + number2 + number3) / 3)
print()

# converting_minutes_to_hours
minutes = int(input("Enter minutes: "))
print("Time:", minutes // 60, "hours",minutes % 60, "minutes")
print()

# discount
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))
finish_price = round(price - price / 100 * discount, 2)
print("Finish price: ", finish_price)
print()

# last_number
number = int(input("Enter a number: "))
print("Last number:", number % 10)
print()

# perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Perimeter: ", (length + width) * 2)
print()

# numbers_in_column
numbers_4 = int(input("Enter four numbers: "))
print("Numbers in a column:")
print(numbers_4 // 1000)
print(numbers_4 % 1000 // 100)
print(numbers_4 % 1000 % 100 // 10)
print(numbers_4 % 1000 % 100 % 10)
