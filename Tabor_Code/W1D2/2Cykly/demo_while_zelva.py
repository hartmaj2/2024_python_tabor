import turtle

turtle.speed(1)
x_souradnice = turtle.xcor()
turtle.write(x_souradnice)

# DEMO 1: co bude delat zelva v nasledujicim kodu???
# HINT: xcor() nam rekne x-souradnici zelvy, 
# HINT: turtle.write(text) zpusobi, ze zelva vypise text nad sebe
# while True:
#     turtle.forward(30)
#     x_souradnice = turtle.xcor()
#     turtle.write(x_souradnice)

# Chceme aby se zelva zastavila, kdyz dosahne souradnice 100
# Ten kod ma ale nejakou vadu
# DEMO 2: co ted? prodebugovat pomoci breakpointu
while x_souradnice != 100:
    turtle.forward(30)
    x_souradnice = turtle.xcor()
    turtle.write(x_souradnice)

# TODO: opravit chybu v DEMO 2


turtle.mainloop()