from B_ClasesCalculadora import calculadora 
import tkinter as tk
from tkinter import messagebox

while True:   
    
    print("\n----------------------------------------------------------------------")

    try:
        num1 = calculadora(int(input("\nINTRODUCE num1: ")))
        num2 = calculadora(int(input("INTRODUCE num2: ")))

        op = int(input("\nQUÉ OPERACIÓN QUIERES HACER: \n\n1. SUMAR\n2. RESTAR\n3. MULTIPLICAR\n4. DIVIDIR\n5. VER NÚMEROS\n\nELIGE UNA OPCIÓN: "))

        if op == 1: print(num1, "+", num2, "\nEL RESULTADO ES: ", calculadora.sumar())
        elif op == 2: print(num1, "-", num2, "\nEL RESULTADO ES: ", calculadora.restar())
        elif op == 3: print(num1, "*", num2, "\nEL RESULTADO ES: ", calculadora.multiplicar())
        elif op == 4: print(num1, "/", num2, "\nEL RESULTADO ES: ", calculadora.dividir())
        elif op == 5: print("\nLOS NUMEROS ELEGIDOS SON: ", calculadora.ver())
        else: print("\nINTRODUCE NÚMERO VÁLIDO")

    
    except ValueError: (print("\nINTRODUCE SÓLO NÚMEROS, CARBÓN"))

