from Calculadora import Calculadora
from Figura import  *
from Animal import *
from BaseDatos import * 

if __name__=='__main__':
    #principio responsabilidad unica
    calculadora = Calculadora()
    print(calculadora.sumar(2,8))
    print(calculadora.restar(5,4))
    print(calculadora.multiplicar(3,3))
    print(calculadora.dividir(10,5))

    #principio sustitución de liskov
    cuadrado=Cuadrado(2)
    print(cuadrado.area())
    print(cuadrado.perimetro())
    rectangulo=Rectangulo(4,5)
    print(rectangulo.area())
    print(rectangulo.perimetro())

    #segregación de interfaces

    perro=Perro()
    perro.comer()
    perro.dormir()
    perro.cazar()

    vaca=Vaca()
    vaca.comer()
    vaca.dormir()
    vaca.pastar()
    
#Principio inversión depedencia   
    baseDatos=BaseDatos()
    mysql=Mysql()
    manejadorDatos=ManejadorDatos()
    manejadorDatos.procesar(mysql)


    
    




