import tkinter as tk
from tkinter import Canvas
import time

# Configuración de la ventana
ANCHO = 800
ALTO = 600
FPS = 60
VELOCIDAD_FRAMES = 1000 // FPS

class Jugador:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = 30
        self.alto = 40
        self.velocidad_y = 0
        self.velocidad_x = 0
        self.en_piso = False
        self.salto_activo = False
        self.id = canvas.create_rectangle(x, y, x + self.ancho, y + self.alto, fill="red", outline="darkred")
        self.puntos = 0
    
    def actualizar(self, plataformas, enemigos):
        # Aplicar gravedad
        self.velocidad_y += 0.4
        
        # Límite de caída
        if self.velocidad_y > 15:
            self.velocidad_y = 15
        
        self.y += self.velocidad_y
        self.x += self.velocidad_x
        
        # Límites de pantalla
        if self.x < 0:
            self.x = 0
        if self.x + self.ancho > ANCHO:
            self.x = ANCHO - self.ancho
        
        # Detectar colisiones con plataformas
        self.en_piso = False
        for plat in plataformas:
            if plat.colisiona(self):
                self.en_piso = True
                self.velocidad_y = 0
                self.y = plat.y - self.alto
                self.salto_activo = False
        
        # Detectar colisiones con enemigos
        for enemigo in enemigos:
            if enemigo.colisiona(self):
                return False  # Game Over
        
        # Moneda bonus
        self.y = max(self.y, -10)
        
        # Game Over si cae
        if self.y > ALTO:
            return False
        
        self.canvas.coords(self.id, self.x, self.y, self.x + self.ancho, self.y + self.alto)
        return True
    
    def saltar(self):
        if self.en_piso and not self.salto_activo:
            self.velocidad_y = -12
            self.salto_activo = True
            self.en_piso = False

class Plataforma:
    def __init__(self, canvas, x, y, ancho, alto, color="green"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.id = canvas.create_rectangle(x, y, x + ancho, y + alto, fill=color, outline="darkgreen")
    
    def colisiona(self, jugador):
        # Colisión desde arriba
        if (jugador.x + jugador.ancho > self.x and
            jugador.x < self.x + self.ancho and
            jugador.y + jugador.alto >= self.y and
            jugador.y + jugador.alto <= self.y + self.alto + 10 and
            jugador.velocidad_y >= 0):
            return True
        return False

class Enemigo:
    def __init__(self, canvas, x, y, rango=100):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = 25
        self.alto = 25
        self.rango = rango
        self.velocidad = 2
        self.direccion = 1
        self.x_inicial = x
        self.id = canvas.create_oval(x, y, x + self.ancho, y + self.alto, fill="red", outline="darkred")
    
    def actualizar(self):
        self.x += self.velocidad * self.direccion
        
        # Cambiar dirección en los límites
        if abs(self.x - self.x_inicial) > self.rango:
            self.direccion *= -1
        
        self.canvas.coords(self.id, self.x, self.y, self.x + self.ancho, self.y + self.alto)
    
    def colisiona(self, jugador):
        return (jugador.x < self.x + self.ancho and
                jugador.x + jugador.ancho > self.x and
                jugador.y < self.y + self.alto and
                jugador.y + jugador.alto > self.y)

class Moneda:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.recolectada = False
        self.id = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="gold", outline="orange")
    
    def colisiona(self, jugador):
        return (jugador.x < self.x + 10 and
                jugador.x + jugador.ancho > self.x - 10 and
                jugador.y < self.y + 10 and
                jugador.y + jugador.alto > self.y - 10)

class Juego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("🍄 SUPER MARIO 🍄")
        self.ventana.geometry(f"{ANCHO}x{ALTO}")
        self.ventana.resizable(False, False)
        
        self.canvas = Canvas(ventana, width=ANCHO, height=ALTO, bg="lightblue")
        self.canvas.pack()
        
        # Crear plataformas (mapa)
        self.plataformas = [
            Plataforma(self.canvas, 0, ALTO - 50, ANCHO, 50, "brown"),  # Piso
            Plataforma(self.canvas, 100, 450, 150, 20, "green"),
            Plataforma(self.canvas, 350, 400, 150, 20, "green"),
            Plataforma(self.canvas, 600, 450, 150, 20, "green"),
            Plataforma(self.canvas, 50, 300, 120, 20, "green"),
            Plataforma(self.canvas, 450, 300, 120, 20, "green"),
            Plataforma(self.canvas, 700, 300, 100, 20, "green"),
            Plataforma(self.canvas, 200, 150, 150, 20, "orange"),  # Bonus
            Plataforma(self.canvas, 550, 150, 150, 20, "green"),
        ]
        
        # Crear enemigos
        self.enemigos = [
            Enemigo(self.canvas, 150, 410, 80),
            Enemigo(self.canvas, 450, 360, 80),
            Enemigo(self.canvas, 700, 410, 80),
        ]
        
        # Crear monedas
        self.monedas = [
            Moneda(self.canvas, 150, 420),
            Moneda(self.canvas, 450, 370),
            Moneda(self.canvas, 150, 270),
            Moneda(self.canvas, 250, 100),
            Moneda(self.canvas, 600, 100),
        ]
        
        # Crear jugador
        self.jugador = Jugador(self.canvas, 50, ALTO - 100)
        
        # Estado del juego
        self.juego_activo = True
        self.puntos = 0
        self.texto_puntos = self.canvas.create_text(50, 20, text=f"Puntos: {self.puntos}", 
                                                    font=("Arial", 16), fill="black")
        
        # Bindear teclas
        self.ventana.bind("<Left>", lambda e: self.mover_izq())
        self.ventana.bind("<Right>", lambda e: self.mover_der())
        self.ventana.bind("<space>", lambda e: self.jugador.saltar())
        self.ventana.bind("<KeyRelease-Left>", lambda e: self.parar())
        self.ventana.bind("<KeyRelease-Right>", lambda e: self.parar())
        
        self.velocidad_x_actual = 0
        
        # Iniciar loop del juego
        self.loop()
    
    def mover_izq(self):
        self.velocidad_x_actual = -4
        self.jugador.velocidad_x = -4
    
    def mover_der(self):
        self.velocidad_x_actual = 4
        self.jugador.velocidad_x = 4
    
    def parar(self):
        self.jugador.velocidad_x = 0
    
    def loop(self):
        if self.juego_activo:
            # Actualizar enemigos
            for enemigo in self.enemigos:
                enemigo.actualizar()
            
            # Actualizar jugador
            if not self.jugador.actualizar(self.plataformas, self.enemigos):
                self.fin_juego()
                return
            
            # Recoger monedas
            for moneda in self.monedas:
                if not moneda.recolectada and moneda.colisiona(self.jugador):
                    moneda.recolectada = True
                    self.canvas.delete(moneda.id)
                    self.puntos += 100
            
            # Actualizar puntos
            self.canvas.itemconfig(self.texto_puntos, text=f"Puntos: {self.puntos}")
            
            self.ventana.after(VELOCIDAD_FRAMES, self.loop)
    
    def fin_juego(self):
        self.juego_activo = False
        self.canvas.delete("all")
        self.canvas.create_text(ANCHO//2, ALTO//2 - 50, text="GAME OVER", 
                               font=("Arial", 60, "bold"), fill="red")
        self.canvas.create_text(ANCHO//2, ALTO//2 + 50, text=f"Puntos finales: {self.puntos}", 
                               font=("Arial", 24), fill="black")

if __name__ == "__main__":
    ventana = tk.Tk()
    juego = Juego(ventana)
    ventana.mainloop()
