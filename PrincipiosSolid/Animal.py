from abc import ABC, abstractmethod


class Animal (ABC):
    @abstractmethod
    def respirar(self):
        pass

    @abstractmethod
    def comer(self):
        pass    
    
    @abstractmethod
    def dormir(self):
        pass



class Carnivoro(Animal):
    @abstractmethod
    def cazar(self):
        pass

class Herbivorio(Animal):
    @abstractmethod
    def pastar(self):
        pass

class Perro(Carnivoro):
    
    def respirar():
        print("el perro esta respirando")

    def comer(self):
        print("El perro esta comiendo")
    def dormir (self):
        print("el perror esta durmiendo")

    def cazar (self):
        print("el perro esta canzando")   

class Vaca(Herbivorio):
    def respirar(self):
        print("la vaca esta respirando")
    def comer(self):
        print("La vaca esta comiendo hierba")

    def dormir(self):
        print("La vaca esta durmiendo") 
    def pastar(self):
        print("La vaca esta pastando")      
