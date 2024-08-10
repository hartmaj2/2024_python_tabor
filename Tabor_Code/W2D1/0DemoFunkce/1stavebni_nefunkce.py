import turtle
turtle.speed(5)

# Prvni se zamysleme, co vlastne tento kod vykresluje?

# Nasledujici kod nema funkce a neda se rozdelit pro Frantu a Karla

turtle.teleport(-100,-100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.teleport(-100,-50)
turtle.setheading(0)
for i in range(3):
    turtle.forward(50)
    turtle.left(120)

turtle.teleport(100,-100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.teleport(100,-75)
turtle.setheading(0)
for i in range(3):
    turtle.forward(25)
    turtle.left(120)

turtle.teleport(100,100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(75)
    turtle.left(90)
turtle.teleport(100,175)
turtle.setheading(0)
for i in range(3):
    turtle.forward(75)
    turtle.left(120)

turtle.teleport(-100,100)
turtle.setheading(0)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.teleport(-100,200)
turtle.setheading(0)
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
