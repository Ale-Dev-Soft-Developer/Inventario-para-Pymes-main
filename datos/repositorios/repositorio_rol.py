from datos.modelos.rol import Rol
from datos.modelos.usuario import Usuario


def listado_roles():
    return Usuario.select()


#nombre es unique asi que me sirve para buscar
def obtener_rol_por_nombre_usuario(nombre_usuario):
    return Rol.get_or_none(Rol.nombre == nombre_usuario)

def desactivar_rol_por_usuario(usuario:Usuario,nombre_usuario):
    pass