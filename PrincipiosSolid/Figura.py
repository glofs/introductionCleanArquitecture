class Figura:
    def area (self):
        pass
    def perimetro(self):
        pass


class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado


    def area(self):
        return self.lado**2

    def perimetro(self):
        return self.lado*4
    

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.altura=altura 
        self.base=base                
   
 
    def area(self):
        return self.base*self.altura


    def perimetro(self):
        return (2*self.base)*(2*self.altura)      