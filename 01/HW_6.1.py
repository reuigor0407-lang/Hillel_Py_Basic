import string

text = input()

letters = text.split("-")
letter_1 = string.ascii_letters.index(letters[0])
letter_2 = string.ascii_letters.index(letters[1])

result = string.ascii_letters[letter_1:letter_2 + 1]
print(result)