from model import User
class CrearUsuario:
    def __init__(self,usuario_repo):
        self.usuario=usuario_repo


    def ejecutar(self,nombre,correo,contraseña):
        user=User(None, nombre, correo,contraseña)
        self.usuario.guardar(user)
        return user