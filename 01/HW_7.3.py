def second_index(text, some_str):
    first = text.find(some_str)
    second = text[first + len(some_str):].find(some_str)
    if second >= 0:
        second_id = first + len(some_str) + second
        return second_id
    else:
        return None
assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo") == 10
print('ОК')