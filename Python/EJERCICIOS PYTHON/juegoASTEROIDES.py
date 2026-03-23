import turtle
import random
import time


# Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("🚀 ESQUIVA ASTEROIDES 🚀")
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.tracer(0)

# Nave
nave = turtle.Turtle()
nave.shape("triangle")
nave.color("green")
nave.penup()
nave.goto(0, -250)
nave.setheading(90)

# Lista de asteroides
asteroides = []

# Puntuación
puntos = 0
nivel = 1
texto = turtle.Turtle()
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(-380, 280)

def mover_izquierda():
    if nave.xcor() > -380:
        nave.setx(nave.xcor() - 20)

def mover_derecha():
    if nave.xcor() < 380:
        nave.setx(nave.xcor() + 20)

def mover_arriba():
    if nave.ycor() < 280:
        nave.sety(nave.ycor() + 20)

def mover_abajo():
    if nave.ycor() > -280:
        nave.sety(nave.ycor() - 20)

def crear_asteroide():
    asteroide = turtle.Turtle()
    asteroide.shape("circle")
    asteroide.color("yellow")
    asteroide.penup()
    asteroide.goto(random.randint(-350, 350), 270)
    asteroide.velocidad = random.uniform(2, 5)
    asteroides.append(asteroide)

# Controles del teclado
pantalla.onkey(mover_izquierda, "Left")
pantalla.onkey(mover_derecha, "Right")
pantalla.onkey(mover_arriba, "Up")
pantalla.onkey(mover_abajo, "Down")
pantalla.listen()

contador = 0
juego_activo = True
colision = False

while juego_activo:
    pantalla.update()
    
    # Crear asteroides
    contador += 1
    velocidad_creacion = max(10, 30 - (nivel * 2))
    
    if contador > velocidad_creacion:
        crear_asteroide()
        contador = 0
    
    # Mover asteroides
    for asteroide in asteroides[:]:
        asteroide.sety(asteroide.ycor() - asteroide.velocidad)
        
        # Verificar colisión con nave
        if asteroide.distance(nave) < 20:
            colision = True
            juego_activo = False
        
        # Eliminar si sale de pantalla
        if asteroide.ycor() < -300:
            asteroide.hideturtle()
            asteroides.remove(asteroide)
            puntos += 10
            
            # Aumentar nivel cada 100 puntos
            if puntos % 100 == 0:
                nivel += 1
    

    time.sleep(0.05)  # 50 milisegundos de delay

    # Actualizar puntuación
    texto.clear()
    texto.goto(-380, 280)
    texto.write(f"Puntos: {puntos} | Nivel: {nivel}", font=("Arial", 14, "normal"))

# Pantalla Game Over
game_over = turtle.Turtle()
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 100)
game_over.write("GAME OVER", align="center", font=("Arial", 50, "bold"))

game_over.goto(0, 20)
game_over.color("white")
game_over.write(f"Puntos finales: {puntos}", align="center", font=("Arial", 24, "normal"))

game_over.goto(0, -30)
game_over.write(f"Nivel alcanzado: {nivel}", align="center", font=("Arial", 24, "normal"))

game_over.goto(0, -100)
game_over.color("green")
game_over.write("Haz clic para cerrar", align="center", font=("Arial", 16, "normal"))

pantalla.update()
pantalla.exitonclick()