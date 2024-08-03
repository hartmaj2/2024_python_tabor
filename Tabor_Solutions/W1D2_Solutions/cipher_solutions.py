def str_to_nums(strng):
    new = ""
    for letter in strng.lower():
        if letter == " ":
            new = new + "0,"
        else:
            new = new + str(ord(letter)-96) + ","
    return new[:-1]

def nums_to_str(strng):
    cisla = strng.split(',')
    res = ""
    for prvek in cisla:
        number = int(prvek)
        if number == 0:
            res += " "
        else:
            res += chr(number + 96)
    return res

def flip_pairs(text):
    encrypted = ""
    for i in range(1,len(text),2):
        encrypted += text[i] + text[i-1]
    if len(text) % 2 == 1:
        encrypted += text[-1]
    return encrypted

# Moznost reseni pomoci ascii - ta je vice programatorska, ale narocnejsi na pochopeni
# def moveLetterByAscii(letter, amount):
#     ascii = ord(letter)
#     order = ascii - 97
#     new_order = (order + amount) % 26
#     new_ascii = new_order + 97
#     return chr(new_ascii)

def shiftTextByAmount(text, amount):
    shifted = ""
    for letter in text:
        shifted += moveLetterBy(letter,amount)
    return shifted

def moveLetterBy(letter, amount):
    if letter == " ":
        return " "
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    order = alphabet.index(letter)
    order += amount
    if order >= 26:
        order -= 26
    return alphabet[order]
