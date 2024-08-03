import turtle
import random

turtle.speed(9)
turtle.color('green')
turtle.shape('turtle')
# TODO: vygeneruj si nahodne cislo od 1 do 4 a podle toho vytiskni, jakym smerem se ma zelva otocit
# potom podle toho cisla vyber smer 0,90,180 nebo 270 a jdi rovne

# cislo = random.randint(1,4)
# if cislo == 1:
#     turtle.setheading(0)
# elif cislo == 2:
#     turtle.setheading(90)
# elif cislo == 3:
#     turtle.setheading(180)
# elif cislo == 4:
#     turtle.setheading(270)
# turtle.forward(100)


# TODO: vloz ten kod do cyklu, ktery budes opakovat nejaky pocet krat
for i in range(100):
    cislo = random.randint(1,3)
    if cislo == 1:
        turtle.right(90)
    elif cislo == 2:
        turtle.left(90)
    turtle.forward(10)

# TODO: ted se ale stava, ze zelva se nekdy vraci, zkus kod prepsat tak, aby se zelva nevracela
# a vzdy bud jela dal stejnym smerem nebo se otocila vlevo/vpravo

turtle.mainloop()