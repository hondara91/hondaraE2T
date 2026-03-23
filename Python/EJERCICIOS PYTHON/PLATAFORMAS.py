import turtle
import time

# Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("🎮 JUEGO DE PLATAFORMAS 🎮")
pantalla.setup(width=800, height=600)
pantalla.bgcolor("lightblue")
pantalla.tracer(0)

# Jugador
jugador = turtle.Turtle()
jugador.shape("square")
jugador.color("green")
jugador.penup()
jugador.goto(0, -200)
jugador.velocidad_x = 0
jugador.velocidad_y = 0
jugador.en_piso = False
jugador.puntos = 0

# Física
gravedad = 0.08
velocidad_salto = 6
velocidad_mov = 2

# Teclas presionadas - simple y directo
movimiento = {"actual": ""}  # "", "izq" o "der"

# Mostrador de puntos
texto_puntos = turtle.Turtle()
texto_puntos.hideturtle()
texto_puntos.color("black")
texto_puntos.penup()

# Funciones de control
def tec_izq_press():
    movimiento["actual"] = "izq"

def tec_der_press():
    movimiento["actual"] = "der"

def parar_movimiento():
    movimiento["actual"] = ""

def tecla_salto():
    if jugador.en_piso:
        jugador.velocidad_y = velocidad_salto

# Bindear teclas
pantalla.onkey(tec_izq_press, "Left")
pantalla.onkey(tec_izq_press, "a")
pantalla.onkey(tec_der_press, "Right")
pantalla.onkey(tec_der_press, "d")
pantalla.onkey(parar_movimiento, "Escape")
pantalla.onkey(tecla_salto, "space")
pantalla.listen()

# Plataformas
plat_list = [
    {"x": 0, "y": -280, "ancho": 800, "alto": 40, "tipo": "normal"},  # Suelo
    {"x": -200, "y": -150, "ancho": 100, "alto": 15, "tipo": "normal"},
    {"x": 200, "y": -150, "ancho": 100, "alto": 15, "tipo": "normal"},
    {"x": -300, "y": -50, "ancho": 80, "alto": 15, "tipo": "bonus"},
    {"x": 300, "y": -50, "ancho": 80, "alto": 15, "tipo": "bonus"},
    {"x": 0, "y": 50, "ancho": 100, "alto": 15, "tipo": "normal"},
    {"x": -250, "y": 150, "ancho": 80, "alto": 15, "tipo": "frágil"},
    {"x": 250, "y": 150, "ancho": 80, "alto": 15, "tipo": "normal"},
    {"x": 0, "y": 250, "ancho": 120, "alto": 15, "tipo": "bonus"},
    {"x": -100, "y": -180, "ancho": 60, "alto": 12, "tipo": "frágil"},
    {"x": 100, "y": -100, "ancho": 60, "alto": 12, "tipo": "frágil"},
]

# Monedas para recoger
coins = [
    {"x": -200, "y": -120, "recolectada": False},
    {"x": 200, "y": -120, "recolectada": False},
    {"x": -300, "y": -20, "recolectada": False},
    {"x": 300, "y": -20, "recolectada": False},
    {"x": 0, "y": 80, "recolectada": False},
    {"x": 0, "y": 280, "recolectada": False},
]

# Dibujar monedas
monedas_graficas = {}
for i, coin in enumerate(coins):
    coin_graft = turtle.Turtle()
    coin_graft.shape("circle")
    coin_graft.color("gold")
    coin_graft.penup()
    coin_graft.shapesize(0.5, 0.5)
    coin_graft.goto(coin["x"], coin["y"])
    monedas_graficas[i] = coin_graft

# Enemigos
class Enemigo:
    def __init__(self, x, y, rango=150):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("red")
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.x = x
        self.y = y
        self.rango_inicial = rango
        self.velocidad = 1.5
        self.direccion = 1
    
    def mover(self):
        self.x += self.velocidad * self.direccion
        if abs(self.x - self.rango_inicial) > 75:
            self.direccion *= -1
        self.turtle.setx(self.x)

enemigos = [
    Enemigo(-200, -120),
    Enemigo(200, -120),
    Enemigo(0, 80),
]

# Dibujar plataformas
for p in plat_list:
    plat = turtle.Turtle()
    plat.shape("square")
    if p["tipo"] == "bonus":
        plat.color("orange")
    elif p["tipo"] == "frágil":
        plat.color("lightgray")
    elif p["y"] == -280:
        plat.color("brown")
    else:
        plat.color("gray")
    plat.penup()
    plat.shapesize(p["alto"]/20, p["ancho"]/20)
    plat.goto(p["x"], p["y"])

def detectar_plataforma():
    """Detecta colisión con plataforma"""
    jugador.en_piso = False
    
    for i, p in enumerate(plat_list):
        if (jugador.xcor() + 10 > p["x"] - p["ancho"]/2 and
            jugador.xcor() - 10 < p["x"] + p["ancho"]/2 and
            jugador.ycor() - 10 <= p["y"] + p["alto"]/2 and
            jugador.ycor() - 10 > p["y"] - 20 and
            jugador.velocidad_y <= 0):
            
            jugador.sety(p["y"] + p["alto"]/2 + 10)
            jugador.velocidad_y = 0
            jugador.en_piso = True
            
            # Bonificación por plataformas especiales
            if p["tipo"] == "bonus":
                jugador.puntos += 50
            elif p["tipo"] == "frágil":
                p["activa"] = False  # La plataforma se desactiva

def detectar_monedas():
    """Detecta si el jugador toca una moneda"""
    for i, coin in enumerate(coins):
        if not coin["recolectada"]:
            distancia = ((jugador.xcor() - coin["x"])**2 + 
                        (jugador.ycor() - coin["y"])**2)**0.5
            if distancia < 15:
                coin["recolectada"] = True
                monedas_graficas[i].hideturtle()
                jugador.puntos += 25

def detectar_enemigos():
    """Detecta colisión con enemigo"""
    for enemigo in enemigos:
        distancia = ((jugador.xcor() - enemigo.turtle.xcor())**2 + 
                     (jugador.ycor() - enemigo.turtle.ycor())**2)**0.5
        if distancia < 20:
            return True
    return False

# Loop principal
juego_activo = True
ultima_altura = -200

while juego_activo:
    pantalla.update()
    
    # Movimiento basado en la dirección actual
    if movimiento["actual"] == "izq":
        if jugador.xcor() > -380:
            jugador.setx(jugador.xcor() - velocidad_mov)
    elif movimiento["actual"] == "der":
        if jugador.xcor() < 380:
            jugador.setx(jugador.xcor() + velocidad_mov)
    
    # Gravedad
    jugador.velocidad_y -= gravedad
    jugador.sety(jugador.ycor() + jugador.velocidad_y)
    
    # Colisiones
    detectar_plataforma()
    detectar_monedas()
    
    # Mover enemigos y detectar colisión
    for enemigo in enemigos:
        enemigo.mover()
    
    if detectar_enemigos():
        juego_activo = False
    
    # Puntos por altura
    if jugador.ycor() > ultima_altura:
        ultima_altura = jugador.ycor()
        jugador.puntos += 2
    
    # Game over si cae
    if jugador.ycor() < -300:
        juego_activo = False
    
    # Dibujar puntos
    texto_puntos.clear()
    texto_puntos.goto(-350, 270)
    monedas_restantes = sum(1 for c in coins if not c["recolectada"])
    texto_puntos.write(f"Puntos: {jugador.puntos} | Monedas: {monedas_restantes}", 
                      font=("Arial", 14, "normal"))
    
    time.sleep(0.05)

# Pantalla Game Over
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(0, 100)
game_over.color("red")
game_over.write("GAME OVER", align="center", font=("Arial", 50, "bold"))

game_over.goto(0, 30)
game_over.color("black")
game_over.write(f"Puntos finales: {jugador.puntos}", align="center", font=("Arial", 20, "normal"))

monedas_totales = sum(1 for c in coins if c["recolectada"])
game_over.goto(0, -10)
game_over.write(f"Monedas recolectadas: {monedas_totales}/{len(coins)}", 
                align="center", font=("Arial", 16, "normal"))

game_over.goto(0, -70)
game_over.color("green")
game_over.write("Click para cerrar", align="center", font=("Arial", 16, "normal"))

pantalla.exitonclick()
