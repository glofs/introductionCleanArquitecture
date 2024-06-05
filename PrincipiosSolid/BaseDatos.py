

class BaseDatos:
    def guardar(self,datos):
        pass

    def leer(self):
        pass    

class ManejadorDatos:
    def procesar(self,base_datos):
        base_datos.guardar("Datos de prueba")
        datos_leidos=base_datos.leer()
        print("los datos leidos son ",datos_leidos)



class Mysql(BaseDatos):

    def __init__(self):
        self.data=""
    def guardar(self, datos):
        self.data=datos
        print("conectado a Mysql!! ","Persistieno la informacion.. ",self.data )

    def leer(self):
        return self.data



class MongoDb(BaseDatos):
    def __init__(self):
        self.data=""
    def guardar(self, datos):
        self.data=datos
        print("conectado a MongoDB!! ","Persistieno la informacion.. ",self.data )

    def leer(self):
        return self.data  