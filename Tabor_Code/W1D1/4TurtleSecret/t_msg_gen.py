from t_msg_letters import *

def draw_a_eq_b(x,y,a,b,size):
    a(x,y,size)
    draw_equal_sign(x+size+10,y+size//2,size)
    b(x+size*2+size//2,y,size)

def draw_pyr_eq_N(x,y,size):
    draw_a_eq_b(x,y,draw_pyramid,draw_N,size)

def draw_house_eq_I(x,y,size):
    draw_a_eq_b(x,y,draw_house,draw_I,size)


def draw_secret_message():
    draw_A(150,-100,50)
    draw_house(-100, 0, 50)
    draw_L(-200,-100,50)
    draw_J(-300, 0, 50)
    draw_house_eq_I(-200,200,30)
    draw_E(250,0,50)
    draw_pyramid(50,-100,50)
    draw_D(170,0,50)
    draw_pyr_eq_N(0,-200,50)