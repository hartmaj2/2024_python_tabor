# Strings
text = "Nosorozec je jenom tlusty jednorozec."
text2 = 'Tohle je taky string'
pismeno = "a"

# 1. Spojovani (concatenation)
print("karel" + "IV")
print(text + text2)

# 2. Budovani retezce po pismenkach
slovo = ""
for i in range(10):
    slovo = slovo + "a"

# 3. Retezce (stringy jsou vlastne jen seznamy)

print(text[4])

for i in range(20):
    print(text2[i])

for pismenko in text2:
    print(pismenko)

# 4. Krajeni (slicing seznamu)
print(text[19:25])

