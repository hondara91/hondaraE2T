"""Script para generar imágenes PNG atractivas para el juego aventura_pixel.py"""

from PIL import Image, ImageDraw
import os

# Crear carpeta assets si no existe
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

def dibujar_sombra(draw, x, y, ancho, alto, color_sombra='#00000040'):
    """Dibuja una sombra debajo de un objeto"""
    draw.ellipse([x, y + alto - 5, x + ancho, y + alto], fill=color_sombra)

def crear_personaje():
    """Crea imagen de personaje (chica/princesa mejorada)"""
    img = Image.new('RGBA', (80, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Cabello largo y ondulado (castaño dorado)
    draw.ellipse([12, 8, 68, 45], fill='#D4A574', outline='#8B6914', width=2)
    
    # Cabeza (piel clara)
    draw.ellipse([22, 15, 58, 45], fill='#FDBCB4', outline='#DAA520', width=2)
    
    # Ojos azules grandes y bonitos
    draw.ellipse([28, 22, 37, 33], fill='#4169E1', outline='#000080', width=1)
    draw.ellipse([43, 22, 52, 33], fill='#4169E1', outline='#000080', width=1)
    draw.ellipse([30, 25, 33, 28], fill='#FFFFFF')  # Brillo
    draw.ellipse([45, 25, 48, 28], fill='#FFFFFF')  # Brillo
    
    # Cejas
    draw.arc([27, 20, 38, 22], 0, 180, fill='#8B6914', width=2)
    draw.arc([42, 20, 53, 22], 0, 180, fill='#8B6914', width=2)
    
    # Nariz pequeña
    draw.line([40, 32, 40, 38], fill='#DAA520', width=1)
    draw.ellipse([38, 38, 42, 40], fill='#DAA520')
    
    # Boca (labios rojos sonriente)
    draw.arc([32, 36, 48, 45], 0, 180, fill='#FF1493', width=2)
    draw.polygon([32, 41, 48, 41, 40, 44], fill='#FF69B4')
    
    # Cuello
    draw.rectangle([36, 43, 44, 50], fill='#FDBCB4', outline='#DAA520', width=1)
    
    # Corpiño purpura con detalles
    draw.rectangle([18, 48, 62, 68], fill='#9932CC', outline='#8B008B', width=2)
    draw.arc([18, 48, 62, 58], 0, 180, fill='#BA55D3', width=2)
    
    # Brazos con manos
    draw.ellipse([12, 50, 20, 75], fill='#FDBCB4', outline='#DAA520', width=1)
    draw.ellipse([60, 50, 68, 75], fill='#FDBCB4', outline='#DAA520', width=1)
    draw.circle([16, 77], 3, fill='#FDBCB4')
    draw.circle([64, 77], 3, fill='#FDBCB4')
    
    # Falda voluminosa (gradiente de rosa)
    draw.polygon([15, 65, 65, 65, 62, 88, 18, 88], fill='#FF69B4', outline='#FF1493', width=2)
    draw.polygon([18, 70, 62, 70, 60, 85, 20, 85], fill='#FFB6D9')
    
    # Zapatos elegantes dorados
    draw.ellipse([20, 85, 33, 98], fill='#FFD700', outline='#8B7500', width=2)
    draw.ellipse([47, 85, 60, 98], fill='#FFD700', outline='#8B7500', width=2)
    draw.ellipse([22, 90, 31, 95], fill='#FFF8DC')  # Reflejo
    draw.ellipse([49, 90, 58, 95], fill='#FFF8DC')  # Reflejo
    
    img.save(os.path.join(ASSETS_DIR, 'personaje.png'))
    print("✓ personaje.png creado (mejorado)")

def crear_enemigo():
    """Crea imagen de enemigo (demonio rojo maligno)"""
    img = Image.new('RGBA', (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Cuerpo rojo demoniaco
    draw.ellipse([8, 12, 42, 38], fill='#DC143C', outline='#8B0000', width=2)
    
    # Punta inferior (cola)
    draw.polygon([15, 35, 25, 48, 35, 35], fill='#DC143C', outline='#8B0000', width=2)
    
    # Cuernos (arriba)
    draw.polygon([12, 10, 10, 0, 15, 8], fill='#8B0000', outline='#660000', width=1)
    draw.polygon([38, 10, 40, 0, 35, 8], fill='#8B0000', outline='#660000', width=1)
    
    # Ojos rojos malvados
    draw.ellipse([14, 18, 20, 25], fill='#FF0000', outline='#FFD700', width=1)
    draw.ellipse([30, 18, 36, 25], fill='#FF0000', outline='#FFD700', width=1)
    draw.polygon([16, 20, 18, 22, 16, 24], fill='#000000')  # Pupila
    draw.polygon([32, 20, 34, 22, 32, 24], fill='#000000')  # Pupila
    
    # Boca malvada
    draw.arc([16, 26, 34, 34], 0, 180, fill='#FFD700', width=2)
    
    # Alas (triangulos oscuros)
    draw.polygon([5, 20, 8, 28, 5, 32], fill='#1C1C1C')
    draw.polygon([45, 20, 42, 28, 45, 32], fill='#1C1C1C')
    
    img.save(os.path.join(ASSETS_DIR, 'enemigo.png'))
    print("✓ enemigo.png creado (demonio)")

def crear_moneda():
    """Crea imagen de moneda (dorada brillante con efecto 3D)"""
    img = Image.new('RGBA', (30, 30), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Sombra
    draw.ellipse([2, 18, 28, 26], fill='#00000030')
    
    # Círculo exterior (borde oscuro)
    draw.ellipse([3, 3, 27, 27], fill='#8B7500', outline='#654321', width=1)
    
    # Círculo principal (dorado brillante)
    draw.ellipse([4, 4, 26, 26], fill='#FFD700', outline='#DAA520', width=2)
    
    # Reflejo superior izquierdo (brillo)
    draw.ellipse([6, 6, 14, 14], fill='#FFFF99')
    
    # Star en el centro (brilla más)
    draw.polygon([15, 8, 17, 14, 23, 14, 18, 18, 20, 24, 15, 20, 10, 24, 12, 18, 7, 14, 13, 14], 
                 fill='#FFA500')
    
    # Patrón de moneda (puntos)
    for i in range(3):
        for j in range(3):
            x = 8 + i * 5
            y = 8 + j * 5
            draw.ellipse([x, y, x+2, y+2], fill='#DAA520')
    
    img.save(os.path.join(ASSETS_DIR, 'moneda.png'))
    print("✓ moneda.png creado (con brillo)")

def crear_fondo():
    """Crea un fondo atractivo con cielo degradado, nubes, montañas y pasto"""
    img = Image.new('RGB', (900, 600), '#87CEEB')
    draw = ImageDraw.Draw(img)
    
    # Cielo degradado (azul más claro arriba)
    for y in range(250):
        color_value = int(135 + (190 - 135) * (y / 250))
        hex_color = f'#{color_value:02x}{color_value + 50:02x}ff'
        draw.rectangle([0, y, 900, y+1], fill=hex_color)
    
    # Sol (amarillo brillante con sombra)
    draw.ellipse([750, 50, 850, 150], fill='#FFD700', outline='#FFA500', width=3)
    draw.ellipse([760, 60, 840, 140], fill='#FFFF99')  # Brillo
    
    # Rayos de sol
    for angle in range(0, 360, 30):
        import math
        x1 = 800 + 60 * math.cos(math.radians(angle))
        y1 = 100 + 60 * math.sin(math.radians(angle))
        x2 = 800 + 80 * math.cos(math.radians(angle))
        y2 = 100 + 80 * math.sin(math.radians(angle))
        draw.line([x1, y1, x2, y2], fill='#FFA500', width=2)
    
    # Montañas al fondo (triangulos)
    draw.polygon([0, 350, 150, 200, 300, 350], fill='#2F4F2F', outline='#1C3C2C', width=2)
    draw.polygon([250, 350, 400, 150, 550, 350], fill='#3D5C3D', outline='#2A4220', width=2)
    draw.polygon([500, 350, 700, 180, 900, 350], fill='#2F4F2F', outline='#1C3C2C', width=2)
    
    # Pasto verde (con gradiente de tonos)
    for y in range(350, 600):
        tonality = int(34 + (50 - 34) * ((y - 350) / 250))
        color = f'#{0:02x}{tonality:02x}{0:02x}'
        draw.rectangle([0, y, 900, y+1], fill=color)
    
    # Nubes blancas (varias)
    clouds = [(100, 80), (300, 120), (550, 90), (750, 130), (150, 150)]
    for cx, cy in clouds:
        # Nube grande
        draw.ellipse([cx, cy, cx+80, cy+40], fill='#FFFFFF', outline='#E0E0E0', width=1)
        draw.ellipse([cx+40, cy-15, cx+120, cy+35], fill='#FFFFFF', outline='#E0E0E0', width=1)
        draw.ellipse([cx+80, cy, cx+140, cy+40], fill='#FFFFFF', outline='#E0E0E0', width=1)
        # Sombra interior
        draw.ellipse([cx+60, cy+20, cx+100, cy+35], fill='#F0F0F0')
    
    # Algunos arboles (tronco y copa)
    trees = [(100, 320), (200, 330), (750, 310), (850, 325)]
    for tx, ty in trees:
        # Tronco
        draw.rectangle([tx-8, ty, tx+8, ty+50], fill='#654321', outline='#3D2817', width=1)
        # Copa (circulo verde)
        draw.ellipse([tx-30, ty-40, tx+30, ty+10], fill='#228B22', outline='#1C6B1C', width=2)
        # Detalle de copa
        draw.ellipse([tx-20, ty-35, tx+20, ty+5], fill='#32CD32')
    
    img.save(os.path.join(ASSETS_DIR, 'fondo.png'))
    print("✓ fondo.png creado (panorama)")

if __name__ == '__main__':
    print("Generando imágenes para el juego...")
    crear_personaje()
    crear_enemigo()
    crear_moneda()
    crear_fondo()
    print("\n✓ Todas las imágenes creadas en assets/")
