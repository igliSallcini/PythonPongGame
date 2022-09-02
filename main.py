# Pong Game - Python
#############################

import turtle

dritare = turtle.Screen()
dritare.title("Pong Game by Python - (Loja Ping-Pong ne Python)")
dritare.bgcolor("black")
dritare.setup(width=800, height=600)
dritare.tracer(0)

# Raketa A
raketa_a = turtle.Turtle()
raketa_a.speed(0)
raketa_a.shape("square")
raketa_a.color("Red")
raketa_a.shapesize(stretch_wid=5, stretch_len=1)
raketa_a.penup()
raketa_a.goto(-350, 0)

# Raketa B
raketa_b = turtle.Turtle()
raketa_b.speed(0)
raketa_b.shape("square")
raketa_b.color("Blue")
raketa_b.shapesize(stretch_wid=5, stretch_len=1)
raketa_b.penup()
raketa_b.goto(350, 0)

# Topi
topi = turtle.Turtle()
topi.speed(0)
topi.shape("square")
topi.color("White")
topi.shapesize(stretch_wid=1, stretch_len=1)
topi.penup()
topi.goto(0, 0)

# Levizjet e topit
topi.lx = 0.1
topi.ly = 0.1

# Funksionet

def raketa_a_lart():
    y = raketa_a.ycor()  # Ne fillim ne percaktojme pozicionin e raketes. nepermjet funksionit builtin te turtle .ycor()
    y += 20  # Meqe do levizim lart, dmth koordinata do shtohet me +
    raketa_a.sety(y)  # Percaktojme koordinaten e re me builtin funksion te turtle .sety(y), ku y brenda kllapes eshte koordinata e re

def raketa_a_poshte():
    y = raketa_a.ycor()
    y += -20
    raketa_a.sety(y)


def raketa_b_lart():
    y = raketa_b.ycor()
    y += 20
    raketa_b.sety(y)


def raketa_b_poshte():
    y = raketa_b.ycor()
    y += -20
    raketa_b.sety(y)


# Me siper ne percaktuam funksionet, por nuk i kemi therritur te ekzekutohen akoma. Keshtu qe krijojme
# veprimet e tastjeres si me poshte

# Veprimet e tastjeres (Keyboard)

dritare.listen()  # kjo ben qe te presi per inputin e tasjteres
dritare.onkeypress(raketa_a_lart, "w")  # Tasti qe do levize raketen A lart do jete "w"
dritare.onkeypress(raketa_a_poshte, "s")  # Tasti qe do levize raketen A poshte do jete "s"
dritare.onkeypress(raketa_b_lart, "Up")  # Tasti qe do levize raketen B lart do jete "8"
dritare.onkeypress(raketa_b_poshte, "Down")  # Tasti qe do levize raketen B poshte do jete "2"

# Main game loop
while True:
    dritare.update()  # Sa here qe loop ekzekutohet updates dritare
    # Levizja e topit
    topi.setx(topi.xcor() + topi.lx)
    topi.sety(topi.ycor() + topi.ly)

    # Kontrolli i bordeve
    if topi.ycor() > 290:
        topi.sety(290)
        topi.ly *= -1
    if topi.ycor() < -290:
        topi.sety(-290)
        topi.ly *= -1
    if topi.xcor() > 390:
        topi.goto(0, 0)
        topi.lx *= -1
    if topi.xcor() < -390:
        topi.goto (0, 0)
        topi.lx *= -1