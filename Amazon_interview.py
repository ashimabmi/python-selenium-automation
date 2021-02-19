def unique_letter(name):
    name_char = {}
    duplicate_chars = []
    unique_characters = []
    for char in name.lower():
        if char in name_char:
            name_char[char] = name_char[char] + 1
        else:
            name_char[char] = 1

    for key, value in name_char.items():
        if value > 1:
            duplicate_chars.append(key)

        elif value == 1:
            unique_characters.append(key)

    if unique_characters == None or len(unique_characters) == 0:
        return ""
    else:
        return unique_characters[0]


print('first unique letter of Google :', unique_letter("Google"))
print('first unique letter of Amazon :', unique_letter("Amazon"))
print('first unique letter of box :', unique_letter("box"))# all letters are unique
print('first unique letter of xoxoxo :', unique_letter("xoxoxo"))# no unique letters
print('first unique letter of zoo :', unique_letter("zoo"))# first letter is unique
print('first unique letter of wood :', unique_letter("wood"))# first and last letters are unique
print('first unique letter of oop :', unique_letter("oop"))#only last letter is unique


assert (unique_letter("Google")) == "l", "Expected word '{}' in message, but got '{}'".format("l", (unique_letter("Google")))
assert (unique_letter("Amazon")) == "m", "Expected word '{}' in message, but got '{}'".format("m", (unique_letter("Amazon")))
assert (unique_letter("xoxoxo")) == "", "Expected word '{}' in message, but got '{}'".format("", (unique_letter("xoxoxo")))
assert (unique_letter("box")) == "b", "Expected word '{}' in message, but got '{}'".format("b", (unique_letter("box")))
assert (unique_letter("zoo")) == "z", "Expected word '{}' in message, but got '{}'".format("z", (unique_letter("zoo")))
assert (unique_letter("wood")) == "w", "Expected word '{}' in message, but got '{}'".format("w", (unique_letter("wood")))
assert (unique_letter("oop")) == "p", "Expected word '{}' in message, but got '{}'".format("p", (unique_letter("oop")))
