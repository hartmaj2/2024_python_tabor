i = 1
print("Janek: Co udela tento program?")
answer = input("Student" + str(i) + ": ")
while answer != "neco hezkeho":
    print("Janek: Spatne!")
    print("Janek: Co teda ten program udela?")
    i = i + 1
    answer = input("Student" + str(i) + ": ")
print("Presne tak! Vy jste ale sikulove!")