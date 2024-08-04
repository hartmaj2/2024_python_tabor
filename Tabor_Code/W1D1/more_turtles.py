import turtle
import random
from typing import List

screen = turtle.Screen()
screen.setup(1920,1080)

turtles : list[turtle.Turtle] = [] 
colors = ['red','green','blue','orange','pink','magenta','grey','black','purple']

for i in range(20):
    smery = [0,90,180,270]
    smer = random.randint(0,3)
    turtles.append(turtle.Turtle())
    turtles[i].shape('turtle')
    turtles[i].setheading(smery[smer])
    turtles[i].speed(0)
    turtles[i].color(colors[i%len(colors)])
    

while True:
    for turt in turtles:
        volba = random.randint(1,3)
        if volba == 1:
            turt.left(20)
        if volba == 2:
            turt.right(20)
        if turt.pos()[0] < -screen.window_width()/2:
            turt.setheading(0)
        if turt.pos()[0] > screen.window_width()/2:
            turt.setheading(180)
        if turt.pos()[1] < -screen.window_height()/2:
            turt.setheading(90)
        if turt.pos()[1] > screen.window_height()/2:
            turt.setheading(270) 
        turt.forward(10)
        
