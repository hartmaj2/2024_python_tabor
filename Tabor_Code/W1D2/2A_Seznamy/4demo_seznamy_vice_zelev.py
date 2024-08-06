import turtle
import random

zelvy = []

for i in range(50):
    zelva = turtle.Turtle()
    zelva.speed(10)
    zelvy.append(zelva)

while True:
    for zelva in zelvy:
        cislo = random.randint(1,3)
        if cislo == 1:
            zelva.left(45)
        if cislo == 2:
            zelva.right(45)
        if cislo == 3:
            zelva.forward(50)


turtle.mainloop()