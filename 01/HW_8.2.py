import string

def is_palindrome(text):
    text = text.lower()

    for symbol in string.punctuation:
        text = text.replace(symbol, "").replace(" ", "")

    return text == text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('OP') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("ОК")