from PIL import Image, ImageDraw

# Crear imagen del personaje (chica rubia)
img_personaje = Image.new('RGBA', (100, 130), (0, 0, 0, 0))
draw = ImageDraw.Draw(img_personaje)

# Zapatos rojos (abajo)
draw.ellipse([(10, 110), (25, 125)], fill=(200, 0, 0), outline=(100, 0, 0))
draw.ellipse([(65, 110), (80, 125)], fill=(200, 0, 0), outline=(100, 0, 0))

# Piernas piel
draw.rectangle([(15, 95), (25, 110)], fill=(255, 220, 150))
draw.rectangle([(65, 95), (75, 110)], fill=(255, 220, 150))

# Falda rosa
draw.polygon([(8, 75), (92, 75), (88, 95), (12, 95)], fill=(255, 105, 180), outline=(255, 20, 147))

# Cintura
draw.rectangle([(8, 72), (92, 78)], fill=(255, 215, 0))

# Corpiño rosa oscuro
draw.rectangle([(10, 50), (90, 72)], fill=(255, 20, 147), outline=(199, 21, 133))

# Brazos
draw.rectangle([(0, 52), (10, 68)], fill=(255, 220, 150), outline=(139, 117, 0))
draw.rectangle([(90, 52), (100, 68)], fill=(255, 220, 150), outline=(139, 117, 0))

# Manos
draw.ellipse([(0, 65), (8, 73)], fill=(255, 220, 150))
draw.ellipse([(92, 65), (100, 73)], fill=(255, 220, 150))

# Cuello
draw.ellipse([(30, 45), (70, 52)], fill=(255, 220, 150), outline=(139, 117, 0))

# Cabeza
draw.ellipse([(20, 15), (80, 50)], fill=(255, 220, 150), outline=(139, 117, 0))

# Cabello superior (parte rígida)
points_cabello = [(25, 20), (75, 20), (72, 8), (28, 8)]
draw.polygon(points_cabello, fill=(255, 215, 0), outline=(218, 165, 32))

# Cabello lateral izquierdo
draw.polygon([(18, 22), (24, 24), (22, 45), (16, 42)], fill=(255, 215, 0), outline=(218, 165, 32))

# Cabello lateral derecho
draw.polygon([(82, 22), (76, 24), (78, 45), (84, 42)], fill=(255, 215, 0), outline=(218, 165, 32))

# Moños rojos
draw.polygon([(30, 15), (35, 8), (40, 15)], fill=(255, 0, 0), outline=(139, 0, 0))
draw.polygon([(60, 15), (65, 8), (70, 15)], fill=(255, 0, 0), outline=(139, 0, 0))

# Ojos azules grandes
draw.ellipse([(30, 28), (42, 38)], fill=(135, 206, 235), outline=(0, 0, 0))
draw.ellipse([(58, 28), (70, 38)], fill=(135, 206, 235), outline=(0, 0, 0))

# Pupilas
draw.ellipse([(36, 32), (40, 36)], fill=(0, 0, 0))
draw.ellipse([(64, 32), (68, 36)], fill=(0, 0, 0))

# Brillo de ojos (destello)
draw.ellipse([(37, 30), (39, 32)], fill=(255, 255, 255))
draw.ellipse([(65, 30), (67, 32)], fill=(255, 255, 255))

# Nariz simple
draw.polygon([(49, 40), (51, 40), (50, 44)], fill=(240, 200, 140))

# Sonrisa
draw.arc([(35, 42), (65, 52)], 0, 180, fill=(255, 100, 150), width=2)

# Mejillas (blush)
draw.ellipse([(22, 36), (30, 42)], fill=(255, 150, 180))
draw.ellipse([(70, 36), (78, 42)], fill=(255, 150, 180))

# Guardar
img_personaje.save('assets/personaje.png')
print("✓ Personaje creado: assets/personaje.png")

# ===== CREAR ENEMIGO (Goomba mejorado) =====
img_enemigo = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
draw_e = ImageDraw.Draw(img_enemigo)

# Caparazón marrón
draw_e.ellipse([(5, 10), (45, 40)], fill=(139, 69, 19), outline=(101, 50, 10))

# Barriga más clara
draw_e.ellipse([(10, 18), (40, 35)], fill=(160, 82, 45), outline=(101, 50, 10))

# Ojos grandes
draw_e.ellipse([(12, 15), (22, 25)], fill=(255, 255, 255), outline=(0, 0, 0))
draw_e.ellipse([(28, 15), (38, 25)], fill=(255, 255, 255), outline=(0, 0, 0))

# Pupilas
draw_e.ellipse([(16, 18), (19, 22)], fill=(0, 0, 0))
draw_e.ellipse([(32, 18), (35, 22)], fill=(0, 0, 0))

# Patas
draw_e.rectangle([(14, 38), (18, 48)], fill=(101, 50, 10))
draw_e.rectangle([(32, 38), (36, 48)], fill=(101, 50, 10))

# Boca
draw_e.line([(20, 30), (30, 30)], fill=(0, 0, 0), width=1)

img_enemigo.save('assets/enemigo.png')
print("✓ Enemigo creado: assets/enemigo.png")

# ===== CREAR MONEDA =====
img_moneda = Image.new('RGBA', (30, 30), (0, 0, 0, 0))
draw_m = ImageDraw.Draw(img_moneda)

# Círculo exterior (oro)
draw_m.ellipse([(2, 2), (28, 28)], fill=(255, 215, 0), outline=(184, 134, 11))

# Patrón de cruz dentro
draw_m.line([(8, 15), (22, 15)], fill=(184, 134, 11), width=2)
draw_m.line([(15, 8), (15, 22)], fill=(184, 134, 11), width=2)

# Pequeños puntos
draw_m.ellipse([(12, 12), (14, 14)], fill=(184, 134, 11))
draw_m.ellipse([(16, 12), (18, 14)], fill=(184, 134, 11))
draw_m.ellipse([(12, 16), (14, 18)], fill=(184, 134, 11))
draw_m.ellipse([(16, 16), (18, 18)], fill=(184, 134, 11))

# Brillo
draw_m.ellipse([(8, 8), (12, 12)], fill=(255, 255, 200))

img_moneda.save('assets/moneda.png')
print("✓ Moneda creada: assets/moneda.png")

print("\n✓✓✓ ¡Todos los gráficos se han creado exitosamente!")
print("Ubicación: assets/personaje.png, assets/enemigo.png, assets/moneda.png")
