class Circulo:
    def __init__(self,radio ):
        self.radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.radio
        

    def CalcularAria(self):
        return self.__pi*self.radio**2