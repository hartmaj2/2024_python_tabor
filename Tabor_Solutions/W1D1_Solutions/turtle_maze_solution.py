## Je potreba mit tento soubor otevreny v GUI i s obrazkami, jinak je soubor neuvidi. 
## Nejlepe kdyz se otevre pomoci File -> Open Folder...
from turtle import *

# Vytvor pozadi
Screen()
title("Turtle Maze")
speed(0)
# Vytvor zelvu

shape("turtle")
color("green")
# player.dot() # Pomoci tecky pozname, kde je pocatek souradnicove soustavy (0,0)
penup()

# Prepinac
picture = 'maze'

# 'square'
# 'star'
# 'open_picture'
# 'multi_uhelnik'
# 'maze'
# 'round_maze'

if picture == 'square':    
    bgpic("pics/turtle_square.png")  # Nastav obrazek na pozadi
    teleport(-145, 150)  # Nastav pocatecni souradnice
    setheading(270) # Nastav pocatecni smer

if picture == 'star':
    bgpic("pics/turtle_star.png")  # Nastav obrazek na pozadi
    teleport(-6, 220)  # Nastav pocatecni souradnice   
    setheading(270) # Nastav pocatecni smer

if picture == 'open_picture':
    bgpic("pics/turtle_openpicture.png")  # Nastav obrazek na pozadi
    teleport(-1, 220)  # Nastav pocatecni souradnice      
    setheading(270) # Nastav pocatecni smer

if picture == 'multi_uhelnik':
    bgpic("pics/turtle_multi_uhelnik.png")  # Nastav obrazek na pozadi
    teleport(-30, 215)  # Nastav pocatecni souradnice            
    setheading(270) # Nastav pocatecni smer

if picture == 'maze':
    bgpic("W1D1_Solutions/turtle_maze.png")  # Nastav obrazek na pozadi
    teleport(-30, 215)  # Nastav pocatecni souradnice
    setheading(270) # Nastav pocatecni smer

if picture == 'round_maze':
    bgpic("pics/turtle_round_maze.png")  # Nastav obrazek na pozadi
    teleport(-30, 215)  # Nastav pocatecni souradnice    
    setheading(270) # Nastav pocatecni smer

def vyres_bludiste():
    pendown()
    forward(10)
    left(90)
    forward(230)
    right(90)
    forward(100)
    right(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(70)
    left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    forward(70)
    left(90)
    forward(100)
    right(90)
    forward(50)
    left(90)
    forward(80)
    left(90)
    forward(50)
    right(90)
    forward(100)
    


# TODO: SEM PRIDEJ SVUJ KOD 
vyres_bludiste()
    
''' Pro pohyb pouzij funkce ''' 
#  player.forward(int) 
#  player.backward(int)

'''  Pro otaceni pouzij funkce: ''' 
#  player.left(int)
#  player.right(int)

''' Pokud zrovna nechces kreslit, napis toto:'''
#  player.penup()
#  pak kresleni znovu vratis takto:
#  player.pendown()

''' Pokud chces zmenit barvu, napis toho:'''
#  player.color('nazev barvy v anglictine')

''' Vlastni promennou definujes takto:'''
#  tvoje_promenna = hodnota

''' Pokud chces vyuzit cykly(loopy), napis je takto: ''' 
#  for i in range(pocet_opakovani):
#       tvuj kod

''' Pokud chces vyuzit podminky(conditions), napis je takto: ''' 
#  if tvoje_podminka:
#       tvuj kod
#  elif tvoje_druha_podminka:
#       tvuj kod
#  else:
#       tvuj kod

''' Pokud chces napsat vlastni funkci, napis ji takto:'''
#  def jmeno_tve_funkce(parametry):
#       tvuj kod 



# Nechej screen zapnuty
mainloop()