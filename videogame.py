from turtle import *
import turtle
import time
import random

posponer = 0.1
score = 0
high_score = 0

#Configuracion de pantalla
class windows():
    windows = True
windows = turtle.Screen()
windows.title("Mi Juego")
windows.bgcolor("purple")
windows.setup(width= 600, height=600)
windows.tracer(0)


#configuracion del la serpiente
class serpiente():
    serpiente = True
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.color("white")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"

#nombre del usuario
nombre = turtle.textinput("Nombre", "Ingresa nombre del jugador: ")

#Comida
class comida():
    comida = True
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#cuerpo serpiente
segmento = []

#texto
class texto():
    texto=True
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score : 0       HighScore: 0", align = "center", font = ("Courier", 24, "normal"))


#nombre usuario
class nombre():
    nombre = True
nombre = turtle.Turtle()
nombre.speed(0)
nombre.color("black")
nombre.penup()
nombre.hideturtle()
nombre.goto(0,260)


#funcion
def arriba():
    serpiente.direction = up
def abajo():
    serpiente.direction = down
def izquirda():
    serpiente.direction = left
def derecha():
    serpiente.direction = right


def mov():
    if serpiente.direction == up:
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == down:
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == left:
        x = serpiente.xcor()
        serpiente.setx(x - 20)
    if serpiente.direction == right:
        x = serpiente.xcor()
        serpiente.setx(x + 20)

#Teclado
windows.listen()
windows.onkeypress( arriba, "Up")
windows.onkeypress( abajo, "Down")
windows.onkeypress( izquirda, "Left")
windows.onkeypress( derecha, "Right")



while True:
    windows.update()

    #limites de los bordes.
    if serpiente.xcor() > 280 or serpiente.xcor() < -280 or serpiente.ycor() > 280 or serpiente.ycor() < -280:
        time.sleep(1)
        serpiente.goto(0,0)
        serpiente.direction = "stop"

        for segmentos in segmento:
            segmento.clear()
            segmentos.goto(900,900)
            

            #Reset
            score=0
            texto.clear()
            texto.write("Score:{}       HighScore:{}".format(score, high_score),
            align = "center", font = ("Courier", 24, "normal"))
            
            

    if serpiente.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)


            #cuerpo de la serpiente
        class nuevo_segmento():
            nuevo_segmento = True
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmento.append(nuevo_segmento)

        #aumentador de marcador
        score += 20

        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score:{}      High Score:{}".format(score, high_score),
        align = "center", font = ("Courier", 24, "normal"))


    
    #movimiento 
    total = len(segmento)
    for index in range(total -1, 0, -1):
        x = segmento[index - 1].xcor()
        y = segmento[index - 1].ycor()
        segmento[index].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        segmento[0].goto(x,y)


    mov()

    #morderse la serpiente
    for segmentos in segmento:
        if segmentos.distance(serpiente) < 20:
            time.sleep(1)
            serpiente.goto(0,0)
            serpiente.direction = "stop"

            segmentos.goto(900,900)
            segmento.clear()


            score = 0
            texto.clear()
            texto.write("Score:{}      High Score:{}".format(score, high_score),
            align = "center", font = ("Courier", 24, "normal"))

    time.sleep(posponer)











