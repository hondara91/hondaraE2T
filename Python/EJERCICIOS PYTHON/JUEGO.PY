import pygame
import random
import math

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🚀 ESQUIVA ASTEROIDES 🚀")
reloj = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)

# Fuente
fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 72)

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTO:
            self.rect.y += self.velocidad

    def dibujar(self, surface):
        pygame.draw.polygon(surface, VERDE, [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.centerx + 10, self.rect.centery),
            (self.rect.right, self.rect.bottom)
        ])


class Asteroide(pygame.sprite.Sprite):
    def __init__(self, x, y, tamaño=3):
        super().__init__()
        self.tamaño = tamaño
        self.radio = 10 * tamaño
        self.image = pygame.Surface((self.radio * 2, self.radio * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, AMARILLO, (self.radio, self.radio), self.radio)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad_x = random.uniform(-2, 2)
        self.velocidad_y = random.uniform(1, 3)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        if self.rect.top > ALTO:
            self.kill()


class Juego:
    def __init__(self):
        self.puntuacion = 0
        self.nivel = 1
        self.nave = Nave()
        self.asteroides = pygame.sprite.Group()
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.nave)
        self.contador_asteroides = 0
        self.juego_activo = True

    def crear_asteroide(self):
        x = random.randint(0, ANCHO)
        y = random.randint(-50, -10)
        asteroide = Asteroide(x, y, tamaño=random.randint(1, 3))
        self.asteroides.add(asteroide)
        self.sprite_group.add(asteroide)

    def verificar_colisiones(self):
        colisiones = pygame.sprite.spritecollide(self.nave, self.asteroides, True)
        if colisiones:
            return False
        return True

    def actualizar(self):
        self.sprite_group.update()
        self.contador_asteroides += 1
        
        # Crear asteroides cada cierto tiempo
        if self.contador_asteroides > 30 - (self.nivel * 3):
            self.crear_asteroide()
            self.contador_asteroides = 0
        
        # Aumentar puntuación
        self.puntuacion += 1
        
        # Aumentar nivel cada 5000 puntos
        if self.puntuacion % 5000 == 0:
            self.nivel += 1

    def dibujar(self):
        pantalla.fill(NEGRO)
        
        # Dibujar nave
        self.nave.dibujar(pantalla)
        
        # Dibujar asteroides
        for asteroide in self.asteroides:
            pygame.draw.circle(pantalla, AMARILLO, asteroide.rect.center, asteroide.radio)
        
        # Dibujar puntuación
        texto_puntos = fuente.render(f"Puntos: {self.puntuacion // 10}", True, BLANCO)
        texto_nivel = fuente.render(f"Nivel: {self.nivel}", True, BLANCO)
        pantalla.blit(texto_puntos, (10, 10))
        pantalla.blit(texto_nivel, (ANCHO - 200, 10))
        
        pygame.display.flip()

    def pantalla_game_over(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return True

            pantalla.fill(NEGRO)
            texto_game_over = fuente_grande.render("GAME OVER", True, ROJO)
            texto_puntos = fuente.render(f"Puntos finales: {self.puntuacion // 10}", True, BLANCO)
            texto_nivel = fuente.render(f"Nivel alcanzado: {self.nivel}", True, BLANCO)
            texto_reiniciar = fuente.render("Presiona ESPACIO para jugar de nuevo o CERRAR para salir", True, VERDE)
            
            pantalla.blit(texto_game_over, (ANCHO // 2 - 200, ALTO // 2 - 100))
            pantalla.blit(texto_puntos, (ANCHO // 2 - 150, ALTO // 2))
            pantalla.blit(texto_nivel, (ANCHO // 2 - 150, ALTO // 2 + 50))
            pantalla.blit(texto_reiniciar, (ANCHO // 2 - 300, ALTO // 2 + 150))
            
            pygame.display.flip()
            reloj.tick(60)

    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            reloj.tick(60)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
            
            if not self.verificar_colisiones():
                if not self.pantalla_game_over():
                    ejecutando = False
                else:
                    # Reiniciar juego
                    self.__init__()
                    continue
            
            self.actualizar()
            self.dibujar()
        
        pygame.quit()


# Ejecutar juego
if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()