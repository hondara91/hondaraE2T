responsables = int(input("DE CUÁNTOS ACCIDENTES HA SIDO RESPONSABLE: "))
años = int(input("CUÁNTOS AÑOS EN LA EMPRESA: ")) 
km = int(input("CUÁNTOS KM HA RECORRIDO: "))
prima_antigüedad = 0
prima_distancia = km * 0.01


if años >= 4: prima_antigüedad = (200 + (años - 4) * 20)
if prima_distancia > 400: prima_distancia = 400

X = prima_antigüedad + prima_distancia

if responsables == 0: extra = X
if responsables == 1: extra = X/2
if responsables == 2: extra = X/3
if responsables == 3: extra = X/4
if responsables > 3: extra = 0

print (extra)