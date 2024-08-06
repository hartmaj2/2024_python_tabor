import turtle

turtle.speed(9)
turtle.color('green')
turtle.shape('turtle')

odpoved = input("Kam chces aby sla zelva? ")
if odpoved == "dopredu":
    turtle.forward(100)
if odpoved == "dozadu":
    turtle.backward(100)


turtle.mainloop() # aby okno zustalo otevrene dokud nezmacknes krizek