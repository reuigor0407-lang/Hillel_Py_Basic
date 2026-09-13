import keyword

text = input("Введiть змiнну: ")

valid = True

if text[0].isdigit():
    valid = False

for symbol in text:
    if symbol.isupper():
        valid = False
    if not symbol.isalnum() and symbol != "_":
        valid = False

if "__" in text:
    valid = False

if text in keyword.kwlist:
    valid = False

print(valid)


