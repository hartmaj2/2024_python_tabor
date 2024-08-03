import turtle

def draw_A(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.backward(size // 2)
    turtle.right(120)
    turtle.forward(size // 2)
    turtle.backward(size // 2)
    turtle.left(60)

def draw_B(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    for _ in range(2):
        turtle.right(90)
        turtle.forward(size // 2)
        turtle.right(90)
        turtle.forward(size // 2)
        turtle.backward(size // 2)


def draw_C(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y + size)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(size // 2, 180)


def draw_D(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.circle(size // 2, 180)

def draw_E(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(size)
    turtle.backward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.backward(size)
    turtle.left(90) 
    turtle.forward(size // 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.circle(size // 2)

def draw_F(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.backward(size)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)


def draw_G(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y + size)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(size // 2, 270)
    turtle.left(90)
    turtle.forward(size // 4)


def draw_H(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.backward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.backward(size)


def draw_I(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(size)
    turtle.backward(size // 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.backward(size // 2)
    turtle.forward(size)


# broken
def draw_J(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y + size)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(size)
    for i in range(4):
        turtle.left(90)
        turtle.forward(size // 4)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_K(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.backward(size // 2)
    turtle.right(45)
    turtle.forward(size // 2)
    turtle.backward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.penup()
    turtle.home()
    turtle.pendown()

# broken
def draw_L(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y + size)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_M(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size // 2 * 1.414)
    turtle.left(90)
    turtle.forward(size // 2 * 1.414)
    turtle.right(135)
    turtle.forward(size)


def draw_N(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size * 1.414)
    turtle.left(135)
    turtle.forward(size)


def draw_O(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y + size // 2)
    turtle.pendown()
    turtle.circle(size // 2)


def draw_P(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)

# pridej kod na nakresleni domecku
def draw_house(x,y,size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x,y)
    turtle.pendown()


def draw_equal_sign(x, y, size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(size)
        turtle.penup()
        turtle.backward(size)
        turtle.right(90)
        turtle.forward(size // 4)
        turtle.left(90)
        turtle.pendown()

# pridej kod na nakresleni pyramidy
def draw_pyramid(x,y,size):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.pendown()
