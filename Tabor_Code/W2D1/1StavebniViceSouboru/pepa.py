import turtle

# Pise Pepa - ten vymysli, jak se stavi pyramida a kostka
def postav_kostku(x,y,velikost):
    turtle.teleport(x,y)
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(velikost)
        turtle.left(90)

def postav_pyramidu(x,y,velikost):
    turtle.teleport(x,y)
    turtle.setheading(0)
    for i in range(3):
        turtle.forward(velikost)
        turtle.left(120)