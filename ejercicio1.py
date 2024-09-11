class Circulo:
    def __init__(self,radio ):
        self.radio = radio
        self.pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.pi*self.radio
        

    def CalcularAria(self):
        return self.pi*self.radio**2
        
c1 =Circulo(2.5)
print(c1.CalcularAria())
print(c1.calcularPerimetro())
print(f"la costante PI es{c1.pi}")