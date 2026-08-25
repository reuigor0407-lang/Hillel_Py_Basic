number_1 = float(input("Enter first numbers:"))
number_2 = float(input("Enter second numbers:"))
action = input("Enter action (+, -, /, *):")

if action == "+":
    print(number_1 + number_2)
elif action == "-":
    print(number_1 - number_2)
elif action == "*":
    print(number_1 * number_2)
elif action == "/":
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("You can't divide by zero")
else:
    print("Wrong action")

print()