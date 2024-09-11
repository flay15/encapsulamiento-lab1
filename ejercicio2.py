class Circulo:
    def __init__(self,radio ):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio
        

    def CalcularAria(self):
        return self.__pi*self.__radio**2
        
c1 =Circulo(2.5)
print(c1.CalcularAria())
print(c1.calcularPerimetro())
print(f"la costante PI es{c1.__pi}")