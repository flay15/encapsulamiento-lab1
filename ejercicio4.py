class Circulo:
    def __init__(self,radio ):
        self.radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.radio
        

    def CalcularAria(self):
        return self.__pi*self.radio**2
    

    def getPi(self):
        return self.__pi
    
    def setradio(self, nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float:
            if nuevoValor > 0:
                self.__radio = nuevoValor
                print(f"El radio se ha modificado correctamente:{self.__radio}")
            else:
                print("El radio no puede ser negativo")
        
        else:

            print("El radio tiene que ser un numero positivo")


            
        
