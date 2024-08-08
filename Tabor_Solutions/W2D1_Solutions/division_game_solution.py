# hra se nezastavi i kdyz dosahneme limitu 0.3 bodu (neptej se proc tak divny limit)
# najdi pomoci debuggeru, co je s kodem za problem
# mozna ma hra jeste dalsi bug, ktery budes muset najit hahaha
import random
points = 0
limit = 0.3
print("Welcome to the Division Game!")
print("You will play until you get 1 point.\n")
while points < limit:
    num2 = random.randint(0,10)
    correct_answer = random.randint(0,10)
    num1 = correct_answer * num2
    print(f"What is {num1} / {num2}?")
    answer = input("Your answer: ")
    if int(answer) == correct_answer:
        points = points + 0.1         
        print(f"Correct!\nYou have {points:.1f} points.\n")
    else:
        print(f"Wrong. The correct answer was {correct_answer}.\n")
print(f"Congratulations")

