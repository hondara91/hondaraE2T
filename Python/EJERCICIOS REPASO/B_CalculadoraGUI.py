import tkinter as tk
from tkinter import messagebox
# Aquí importamos la clase de nuestra calculadora
from B_ClasesCalculadora import Calculadora

class CalculadoraGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora POO")
        self.root.geometry("320x420")

        # Etiquetas y entradas
        tk.Label(self.root, text="Número 1:", font=("Arial", 12)).pack(pady=10)
        self.entry1 = tk.Entry(self.root, font=("Arial", 14), width=15, justify="center")
        self.entry1.pack()

        tk.Label(self.root, text="Número 2:", font=("Arial", 12)).pack(pady=10)
        self.entry2 = tk.Entry(self.root, font=("Arial", 14), width=15, justify="center")
        self.entry2.pack()

        # Botones
        tk.Button(self.root, text="Sumar",      width=15, font=("Arial", 12), command=self.calcular_suma).pack(pady=8)
        tk.Button(self.root, text="Restar",     width=15, font=("Arial", 12), command=self.calcular_resta).pack(pady=5)
        tk.Button(self.root, text="Multiplicar",width=15, font=("Arial", 12), command=self.calcular_multiplicacion).pack(pady=5)
        tk.Button(self.root, text="Dividir",    width=15, font=("Arial", 12), command=self.calcular_division).pack(pady=5)

        # Resultado
        self.resultado_label = tk.Label(self.root, text="Resultado: ", font=("Arial", 14, "bold"))
        self.resultado_label.pack(pady=30)

        self.root.mainloop()

    def get_numeros(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
            return None, None

    # Métodos que llaman a los métodos de la clase Calculadora instanciándola en cada llamada
    def calcular_suma(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.sumar()
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def calcular_resta(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.restar()
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def calcular_multiplicacion(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.multiplicar()
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def calcular_division(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.dividir()
            self.resultado_label.config(text=f"Resultado: {resultado}")

if __name__ == "__main__":
    CalculadoraGUI()