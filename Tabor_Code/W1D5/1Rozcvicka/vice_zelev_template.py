import turtle
from turtle import Turtle
import random 
screen = turtle.Screen()

# Zelev si muzeme udelat vice. Do kazde promenne si muzeme ulozit objekt, ktery odpovida zelve
# Objekt ma v sobe ulozene informace jako barva, tvar, pozice atd.
# Objekt muze take vykonavat funkce, ktere podporuje jako color(), speed() atd

prvni = turtle.Turtle() 
druha = turtle.Turtle()
treti = turtle.Turtle()


# TODO: nastav zelvam postupne barvy ze seznamu barvy, a vsem dej rychlost 10
zelvy = [prvni,druha,treti]
barvy = ['red','green','blue']

for i in range(0,2):
    ...


# TODO: rozmisti zelvy nahodne po obrazovce, pouzij goto()
for zelva in zelvy:
    ...


# TODO: napis funkci, ktera prijme jako parametr zelvu a pote s ni udela jeden krok opile zelvy
def udelej_krok(zelva: Turtle):
    ...

# TODO: nyni donekonecna provadej pro kazdou zelvu jeji krok, 
# tento nekonecny cyklus se pouziva pri tvorbe her a rika se mu necekane game loop neboli herni smycka
while True:
    ...

screen.mainloop()