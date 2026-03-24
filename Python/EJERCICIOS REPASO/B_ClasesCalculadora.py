class calculadora:

    def __init__(self, value): self.valor = value
    def sumar(): return int(num1.valor) + int(num2.valor)
    def restar(): return int(num1.valor) - int(num2.valor)
    def multiplicar(): return int(num1.valor) * int(num2.valor)
    def dividir(): return int(num1.valor) / int(num2.valor)
    def ver(): return str(num1.valor) + " y " + str(num2.valor)  
    def __str__(self): return str(self.valor)


class Calculadora:

    def __init__(self, value1, value2):
        self.valor1 = value1
        self.valor2 = value2

    def sumar(self): return int(self.valor1) + int(self.valor2)
    def restar(self): return  int(self.valor1) - int(self.valor2)
    def multiplicar(self): return  int(self.valor1) * int(self.valor2)
    def dividir(self): return  int(self.valor1) / int(self.valor2)