import string

text = input("Write a sentence: ")
text = text.title()

for symbol in string.punctuation:
    text = text.replace(symbol, "").replace(" ", "")

text = "#" + text

if len(text) > 140:
    text = text[:140]

print(text)
