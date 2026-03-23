import tkinter as tk
from tkinter import Canvas
import math
import os

try:
    from PIL import Image, ImageTk
    TIENE_PIL = True
except ImportError:
    TIENE_PIL = False

# Directorio de assets (imágenes)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def cargar_imagen(nombre, tamanio=None):
    """Cargar imagen PNG de la carpeta assets (si existe)."""
    if not TIENE_PIL:
        return None
    ruta = os.path.join(ASSETS_DIR, nombre)
    if not os.path.exists(ruta):
        return None
    try:
        img = Image.open(ruta).convert("RGBA")
        if tamanio is not None:
            img = img.resize(tamanio, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

ANCHO = 900
ALTO = 600
FPS = 120
VELOCIDAD_FRAMES = 1000 // FPS

# Intento de cargar sprites desde assets/
IMG_PERSONAJE = cargar_imagen("personaje.png", (80, 100))
IMG_ENEMIGO = cargar_imagen("enemigo.png", (50, 50))
IMG_MONEDA = cargar_imagen("moneda.png", (30, 30))

class Personaje:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = 35
        self.alto = 45
        self.velocidad_y = 0
        self.velocidad_x = 0
        self.en_piso = False
        self.salto_activo = False
        self.puntos = 0
        self.animacion = 0
        self.elementos = []  # Guardar todos los elementos

        # Usar sprite si está disponible
        self.use_image = IMG_PERSONAJE is not None
        if self.use_image:
            self.photo = IMG_PERSONAJE
            self.id = self.canvas.create_image(self.x, self.y, image=self.photo, anchor="nw")
        else:
            self.dibujar()  # Dibujar al crear
    
    def dibujar(self):
        """Dibuja una chica rubia tipo princesa"""
        # Zapatos rojos
        zapato_izq = self.canvas.create_oval(
            self.x + 6, self.y + 38, self.x + 14, self.y + 45,
            fill="#CC0000", outline="#660000", width=2
        )
        self.elementos.append(zapato_izq)
        
        zapato_der = self.canvas.create_oval(
            self.x + 21, self.y + 38, self.x + 29, self.y + 45,
            fill="#CC0000", outline="#660000", width=2
        )
        self.elementos.append(zapato_der)
        
        # Falda/vestido rosa
        falda = self.canvas.create_polygon(
            self.x + 5, self.y + 24,
            self.x + 30, self.y + 24,
            self.x + 32, self.y + 38,
            self.x + 3, self.y + 38,
            fill="#FF69B4", outline="#FF1493", width=2
        )
        self.elementos.append(falda)
        
        # Correa/cintura
        cintura = self.canvas.create_rectangle(
            self.x + 5, self.y + 22, self.x + 30, self.y + 25,
            fill="#FFD700", outline="#8B7500", width=1
        )
        self.elementos.append(cintura)
        
        # Cuerpo/Corpiño rosa oscuro
        corpiño = self.canvas.create_rectangle(
            self.x + 6, self.y + 14, self.x + 29, self.y + 23,
            fill="#FF1493", outline="#C71585", width=2
        )
        self.elementos.append(corpiño)
        
        # Brazos (mangos cortos)
        brazo_izq = self.canvas.create_rectangle(
            self.x - 2, self.y + 15, self.x + 5, self.y + 22,
            fill="#FFDD99", outline="#8B7500", width=2
        )
        self.elementos.append(brazo_izq)
        
        brazo_der = self.canvas.create_rectangle(
            self.x + 30, self.y + 15, self.x + 37, self.y + 22,
            fill="#FFDD99", outline="#8B7500", width=2
        )
        self.elementos.append(brazo_der)
        
        # Cuello
        cuello = self.canvas.create_oval(
            self.x + 10, self.y + 10, self.x + 25, self.y + 15,
            fill="#FFDD99", outline="#8B7500", width=2
        )
        self.elementos.append(cuello)
        
        # Cabeza redondeada
        cabeza = self.canvas.create_oval(
            self.x + 4, self.y - 5, self.x + 31, self.y + 12,
            fill="#FFDD99", outline="#8B7500", width=2
        )
        self.elementos.append(cabeza)
        
        # Cabello rubio (parte superior)
        cabello_arriba = self.canvas.create_polygon(
            self.x + 5, self.y - 1,
            self.x + 30, self.y - 1,
            self.x + 28, self.y - 8,
            self.x + 7, self.y - 8,
            fill="#FFD700", outline="#DAA520", width=2
        )
        self.elementos.append(cabello_arriba)
        
        # Cabello lateral izquierdo
        cabello_izq = self.canvas.create_polygon(
            self.x + 3, self.y + 1,
            self.x + 5, self.y + 1,
            self.x + 6, self.y + 10,
            self.x + 4, self.y + 10,
            fill="#FFD700", outline="#DAA520", width=1
        )
        self.elementos.append(cabello_izq)
        
        # Cabello lateral derecho
        cabello_der = self.canvas.create_polygon(
            self.x + 30, self.y + 1,
            self.x + 32, self.y + 1,
            self.x + 31, self.y + 10,
            self.x + 29, self.y + 10,
            fill="#FFD700", outline="#DAA520", width=1
        )
        self.elementos.append(cabello_der)
        
        # Moño/lazo rojo en el cabello
        moño_izq = self.canvas.create_polygon(
            self.x + 10, self.y - 3,
            self.x + 12, self.y - 5,
            self.x + 13, self.y - 3,
            fill="#FF0000", outline="#8B0000", width=1
        )
        self.elementos.append(moño_izq)
        
        moño_der = self.canvas.create_polygon(
            self.x + 22, self.y - 3,
            self.x + 24, self.y - 5,
            self.x + 25, self.y - 3,
            fill="#FF0000", outline="#8B0000", width=1
        )
        self.elementos.append(moño_der)
        
        # Ojo izquierdo (azul claro)
        ojo_izq = self.canvas.create_oval(
            self.x + 10, self.y + 2, self.x + 16, self.y + 8,
            fill="#87CEEB", outline="black", width=1
        )
        self.elementos.append(ojo_izq)
        
        # Pupila izquierda (se orienta según la dirección)
        offset = 2 if self.velocidad_x >= 0 else -1
        pupi_izq = self.canvas.create_oval(
            self.x + 12 + offset, self.y + 4, self.x + 15 + offset, self.y + 7,
            fill="black"
        )
        self.elementos.append(pupi_izq)
        
        # Ojo derecho (azul claro)
        ojo_der = self.canvas.create_oval(
            self.x + 19, self.y + 2, self.x + 25, self.y + 8,
            fill="#87CEEB", outline="black", width=1
        )
        self.elementos.append(ojo_der)
        
        # Pupila derecha
        pupi_der = self.canvas.create_oval(
            self.x + 21 + offset, self.y + 4, self.x + 24 + offset, self.y + 7,
            fill="black"
        )
        self.elementos.append(pupi_der)
        
        # Sonrisa
        sonrisa = self.canvas.create_arc(
            self.x + 12, self.y + 7, self.x + 23, self.y + 11,
            start=0, extent=180, fill="#FFB6C1", outline="black", width=1
        )
        self.elementos.append(sonrisa)
    
    def actualizar(self, plataformas, enemigos):
        # Actualizar animación
        self.animacion += 1
        
        # Aplicar gravedad
        self.velocidad_y += 0.5
        if self.velocidad_y > 15:
            self.velocidad_y = 15
        
        self.y += self.velocidad_y
        self.x += self.velocidad_x
        
        # Límites de pantalla
        if self.x < 0:
            self.x = 0
        if self.x + self.ancho > ANCHO:
            self.x = ANCHO - self.ancho
        
        # Detectar colisiones
        self.en_piso = False
        for plat in plataformas:
            if plat.colisiona(self):
                self.en_piso = True
                self.velocidad_y = 0
                self.y = plat.y - self.alto
                self.salto_activo = False
        
        # Colisiones con enemigos
        for enemigo in enemigos:
            if enemigo.colisiona(self):
                return False
        
        # Game Over si cae
        if self.y > ALTO:
            return False
        
        self.dibujar_en_posicion()
        return True
    
    def dibujar_en_posicion(self):
        """Redibujar el personaje en la nueva posición"""
        if self.use_image:
            self.canvas.coords(self.id, self.x, self.y)
            return

        # Eliminar elementos anteriores
        for elem in self.elementos:
            self.canvas.delete(elem)
        self.elementos = []

        # Redibujar
        self.dibujar()
    
    def saltar(self):
        if self.en_piso and not self.salto_activo:
            self.velocidad_y = -13
            self.salto_activo = True
            self.en_piso = False

class Plataforma:
    def __init__(self, canvas, x, y, ancho, alto, color="#228B22"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        
        # Dibujar plataforma con patrón de bloques
        self.id_principal = canvas.create_rectangle(
            x, y, x + ancho, y + alto,
            fill=color, outline="#004D00", width=2
        )
        
        # Agregar detalles (pequeños bloques)
        for i in range(0, ancho, 20):
            canvas.create_line(x + i, y, x + i, y + alto, fill="#004D00", width=1)
    
    def colisiona(self, personaje):
        return (personaje.x + personaje.ancho > self.x and
                personaje.x < self.x + self.ancho and
                personaje.y + personaje.alto >= self.y and
                personaje.y + personaje.alto <= self.y + self.alto + 10 and
                personaje.velocidad_y >= 0)

class Enemigo:
    def __init__(self, canvas, x, y, rango=120, tipo="goomba"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = 30
        self.alto = 25
        self.rango = rango
        self.velocidad = 2
        self.direccion = 1
        self.x_inicial = x
        self.tipo = tipo
        self.animacion = 0
        self.elementos = []

        # Usar sprite si está disponible
        self.use_image = IMG_ENEMIGO is not None
        if self.use_image:
            self.photo = IMG_ENEMIGO
            self.id = self.canvas.create_image(self.x, self.y, image=self.photo, anchor="nw")
        else:
            self.dibujar()
    
    def dibujar(self):
        if self.tipo == "goomba":
            # Caparazón marrón redondeado
            caparazon = self.canvas.create_oval(
                self.x + 2, self.y - 2, self.x + self.ancho - 2, self.y + self.alto - 5,
                fill="#8B4513", outline="#654321", width=2
            )
            self.elementos.append(caparazon)
            
            # Parte frontal/barriga
            barriga = self.canvas.create_oval(
                self.x + 5, self.y + 5, self.x + self.ancho - 5, self.y + self.alto - 6,
                fill="#A0522D", outline="#654321", width=1
            )
            self.elementos.append(barriga)
            
            # Ojo izquierdo (blanco grande)
            ojo_izq = self.canvas.create_oval(
                self.x + 6, self.y + 3, self.x + 12, self.y + 9,
                fill="white", outline="black", width=1
            )
            self.elementos.append(ojo_izq)
            
            pupi_izq = self.canvas.create_oval(
                self.x + 7 + (2 if self.direccion == 1 else -2), 
                self.y + 4, 
                self.x + 10 + (2 if self.direccion == 1 else -2), 
                self.y + 8, 
                fill="black"
            )
            self.elementos.append(pupi_izq)
            
            # Ojo derecho (blanco grande)
            ojo_der = self.canvas.create_oval(
                self.x + 18, self.y + 3, self.x + 24, self.y + 9,
                fill="white", outline="black", width=1
            )
            self.elementos.append(ojo_der)
            
            pupi_der = self.canvas.create_oval(
                self.x + 19 + (2 if self.direccion == 1 else -2), 
                self.y + 4, 
                self.x + 22 + (2 if self.direccion == 1 else -2), 
                self.y + 8, 
                fill="black"
            )
            self.elementos.append(pupi_der)
            
            # Patas
            pata_izq = self.canvas.create_rectangle(
                self.x + 8, self.y + self.alto - 4, self.x + 11, self.y + self.alto,
                fill="#654321", outline="#3D2817"
            )
            self.elementos.append(pata_izq)
            
            pata_der = self.canvas.create_rectangle(
                self.x + 19, self.y + self.alto - 4, self.x + 22, self.y + self.alto,
                fill="#654321", outline="#3D2817"
            )
            self.elementos.append(pata_der)
    
    def actualizar(self):
        dx = self.velocidad * self.direccion
        self.x += dx
        self.animacion += 1

        if abs(self.x - self.x_inicial) > self.rango:
            self.direccion *= -1
            dx = -dx

        if self.use_image:
            # Mover el sprite en lugar de redibujar
            self.canvas.move(self.id, dx, 0)
        else:
            # Eliminar elementos anteriores y redibujar
            for elem in self.elementos:
                self.canvas.delete(elem)
            self.elementos = []
            self.dibujar()

    def colisiona(self, personaje):
        return (personaje.x < self.x + self.ancho and
                personaje.x + personaje.ancho > self.x and
                personaje.y < self.y + self.alto and
                personaje.y + personaje.alto > self.y)

class Moneda:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.recolectada = False
        self.animacion = 0

        # Usar sprite si está disponible
        self.use_image = IMG_MONEDA is not None
        if self.use_image:
            self.photo = IMG_MONEDA
            self.id = self.canvas.create_image(self.x, self.y, image=self.photo, anchor="center")
        else:
            self.id = canvas.create_oval(
                x - 7, y - 7, x + 7, y + 7,
                fill="#FFD700", outline="#FFA500", width=2
            )

    def animar(self):
        """Hacer que la moneda brille"""
        if self.recolectada:
            return

        self.animacion = (self.animacion + 1) % 20
        if not self.use_image:
            if self.animacion < 10:
                self.canvas.itemconfig(self.id, fill="#FFD700")
            else:
                self.canvas.itemconfig(self.id, fill="#FFED4E")
    
    def colisiona(self, personaje):
        return (personaje.x < self.x + 12 and
                personaje.x + personaje.ancho > self.x - 12 and
                personaje.y < self.y + 12 and
                personaje.y + personaje.alto > self.y - 12)

class Juego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("🍄 AVENTURA PIXEL 🍄")
        self.ventana.geometry(f"{ANCHO}x{ALTO}")
        self.ventana.resizable(False, False)
        
        self.canvas = Canvas(ventana, width=ANCHO, height=ALTO, bg="#87CEEB")
        self.canvas.pack()
        
        # Variables del juego
        self.juego_activo = False
        self.puntos = 0
        self.personaje = None
        self.plataformas = []
        self.enemigos = []
        self.monedas = []
        self.texto_puntos = None
        
        # Mostrar menú inicial
        self.mostrar_menu()
    
    def mostrar_menu(self):
        """Mostrar menú inicial"""
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, ANCHO, ALTO, fill="#87CEEB")
        
        # Título
        self.canvas.create_text(
            ANCHO//2, 100,
            text="🍄 AVENTURA PIXEL 🍄",
            font=("Arial", 50, "bold"), fill="#FF2828"
        )
        
        # Instrucciones
        self.canvas.create_text(
            ANCHO//2, 250,
            text="← → MUÉVETE | ESPACIO SALTA",
            font=("Arial", 20), fill="black"
        )
        
        # Objetivo
        self.canvas.create_text(
            ANCHO//2, 350,
            text="Recoge monedas y evita enemigos",
            font=("Arial", 16), fill="black"
        )
        
        # Botón de inicio
        self.boton_iniciar = self.canvas.create_rectangle(
            ANCHO//2 - 80, 450, ANCHO//2 + 80, 520,
            fill="#FFD700", outline="#8B7500", width=3
        )
        self.canvas.create_text(
            ANCHO//2, 485,
            text="JUGAR (CLICK)",
            font=("Arial", 18, "bold"), fill="black"
        )
        
        # Bindear click
        self.canvas.bind("<Button-1>", self.click_menu)
        self.canvas.focus_set()
    
    def click_menu(self, event):
        """Detectar click en el botón de inicio"""
        # Si hace click en el botón, iniciar juego
        if ANCHO//2 - 80 < event.x < ANCHO//2 + 80 and 450 < event.y < 520:
            self.iniciar_juego()
    
    def iniciar_juego(self):
        """Inicializar todo para el juego"""
        self.canvas.delete("all")
        
        # Dibujar fondo
        self.canvas.create_rectangle(0, ALTO-40, ANCHO, ALTO, fill="#FFDD00", outline="#FFD700", width=2)
        
        # Crear plataformas
        self.plataformas = [
            Plataforma(self.canvas, 0, ALTO - 60, ANCHO, 60, "#228B22"),  # Piso
            Plataforma(self.canvas, 80, 480, 180, 25, "#228B22"),
            Plataforma(self.canvas, 360, 420, 180, 25, "#228B22"),
            Plataforma(self.canvas, 640, 480, 180, 25, "#228B22"),
            Plataforma(self.canvas, 40, 320, 140, 25, "#228B22"),
            Plataforma(self.canvas, 500, 320, 140, 25, "#228B22"),
            Plataforma(self.canvas, 750, 340, 120, 25, "#228B22"),
            Plataforma(self.canvas, 200, 180, 180, 25, "#FFD700"),  # Oro/bonus
            Plataforma(self.canvas, 600, 180, 180, 25, "#228B22"),
            Plataforma(self.canvas, 400, 80, 100, 25, "#FF6B6B"),  # Rojo/especial
        ]
        
        # Crear enemigos
        self.enemigos = [
            Enemigo(self.canvas, 130, 445, 100, "goomba"),
            Enemigo(self.canvas, 420, 385, 100, "goomba"),
            Enemigo(self.canvas, 700, 445, 100, "goomba"),
            Enemigo(self.canvas, 150, 285, 80, "goomba"),
            Enemigo(self.canvas, 550, 285, 80, "goomba"),
        ]
        
        # Crear monedas
        self.monedas = [
            Moneda(self.canvas, 150, 450),
            Moneda(self.canvas, 450, 390),
            Moneda(self.canvas, 750, 450),
            Moneda(self.canvas, 110, 290),
            Moneda(self.canvas, 200, 140),
            Moneda(self.canvas, 650, 140),
            Moneda(self.canvas, 450, 40),
        ]
        
        # Crear personaje
        self.personaje = Personaje(self.canvas, 50, ALTO - 120)
        
        # Reset de estado
        self.juego_activo = True
        self.puntos = 0
        self.texto_puntos = self.canvas.create_text(
            50, 30, text=f"Puntos: {self.puntos}",
            font=("Arial", 18, "bold"), fill="white"
        )
        self.texto_instrucciones = self.canvas.create_text(
            ANCHO - 150, 30, text="← → MOVE  SPACE JUMP",
            font=("Arial", 11), fill="white"
        )
        
        # Limpiar bindings anteriores y crear nuevos
        self.ventana.bind("<Left>", lambda e: self.mover_izq())
        self.ventana.bind("<Right>", lambda e: self.mover_der())
        self.ventana.bind("<space>", lambda e: self.personaje.saltar())
        self.ventana.bind("<KeyRelease-Left>", lambda e: self.parar())
        self.ventana.bind("<KeyRelease-Right>", lambda e: self.parar())
        self.canvas.unbind("<Button-1>")
        
        # Iniciar loop
        self.loop()
    
    def mover_izq(self):
        self.personaje.velocidad_x = -4
    
    def mover_der(self):
        self.personaje.velocidad_x = 4
    
    def parar(self):
        self.personaje.velocidad_x = 0
    
    def loop(self):
        if self.juego_activo:
            # Actualizar
            for enemigo in self.enemigos:
                enemigo.actualizar()
            
            for moneda in self.monedas:
                moneda.animar()
            
            if not self.personaje.actualizar(self.plataformas, self.enemigos):
                self.fin_juego()
                return
            
            # Recoger monedas
            for moneda in self.monedas:
                if not moneda.recolectada and moneda.colisiona(self.personaje):
                    moneda.recolectada = True
                    self.canvas.delete(moneda.id)
                    self.puntos += 100
            
            self.canvas.itemconfig(self.texto_puntos, text=f"Puntos: {self.puntos}")
            
            self.ventana.after(VELOCIDAD_FRAMES, self.loop)
    
    def fin_juego(self):
        self.juego_activo = False
        self.canvas.create_rectangle(
            ANCHO//2 - 200, ALTO//2 - 100,
            ANCHO//2 + 200, ALTO//2 + 100,
            fill="black", outline="white", width=3
        )
        self.canvas.create_text(
            ANCHO//2, ALTO//2 - 30,
            text="GAME OVER",
            font=("Arial", 50, "bold"), fill="red"
        )
        self.canvas.create_text(
            ANCHO//2, ALTO//2 + 40,
            text=f"Puntos: {self.puntos}",
            font=("Arial", 30), fill="white"
        )

if __name__ == "__main__":
    ventana = tk.Tk()
    juego = Juego(ventana)
    ventana.mainloop()
