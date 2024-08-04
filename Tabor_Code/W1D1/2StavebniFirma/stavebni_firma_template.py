# Jsi stavebni firma a budes dostavat zakazky budov, ktere mas postavit
# Pokud jsi pokrocili, tak se ti bude hodit vyuzit funkce 
# Zkust splnit co nejvice zakazek, ktere dostanes na kartickach
# Dokazem to postavit? Jasne ze (ne)dokazem!

import math
import turtle
turtle.shape('turtle')
turtle.color('green')

# TODO: VYMEN KOD NIZE ZA SVUJ
def napis_L():
    turtle.setheading(270)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)

napis_L()
turtle.teleport(-200,100)
napis_L()

''' Pro pohyb pouzij funkce ''' 
#  turtle.forward(int) 
#  turtle.backward(int)

'''  Pro otaceni pouzij funkce: ''' 
#  turtle.left(int)
#  turtle.right(int)

''' Pokud zrovna nechces kreslit, napis toto:'''
#  turtle.penup()
#  pak kresleni znovu vratis takto:
#  turtle.pendown()

''' Pokud chces zmenit barvu, napis toho:'''
#  turtle.color('nazev barvy v anglictine')

''' Pokud chces zmenit rychlost zelvy, napis toho:'''
#  turtle.speed(int)

''' Vlastni promennou definujes takto:'''
#  tvoje_promenna = hodnota

''' Pokud chces vyuzit cykly(loopy), napis je takto: ''' 
#  for i in range(pocet_opakovani):
#       tvuj kod

''' Dokumentace dalsich funkci je zde: https://docs.python.org/3/library/turtle.html# '''

''' Pokud chces vyuzit podminky(conditions), napis je takto: ''' 
#  if tvoje_podminka:
#       tvuj kod
#  elif tvoje_druha_podminka:
#       tvuj kod
#  else:
#       tvuj kod

''' Pokud chces definovat vlastni funkci, napis ji takto:'''
#  def jmeno_tve_funkce(parametry):
#       tvuj kod 

''' Pokud chces svoji funkci provest napis:'''
#  jmeno_tve_funkce(parametry)

# Nechej screen zapnuty
turtle.mainloop()

# EXTRA CHALLENGE TODO: Nakresli domecek jednim tahem
# HINT: pytagoras je tvuj kamarad (uz je mrtvej, ale jeho veta je uzitecna)
# HINT2: odmocnina se dela pomoci funkce math.sqrt(int)