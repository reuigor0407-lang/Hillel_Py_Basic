import string
def first_word(text):
    for symbol in string.punctuation:
        if symbol != "'":
            text = text.replace(symbol, " ")
    text = text.strip(string.punctuation).split()
    return text[0]

assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word(".., and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print('OK')

