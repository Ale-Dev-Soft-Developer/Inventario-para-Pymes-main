from datos.modelos.rol import Rol
from datos.modelos.usuario import Usuario
from peewee import (IntegrityError,
                    OperationalError,
                    DataError,
                    PeeweeException)
from auxiliares.mensajes import (excepcion_data_error,
                                excepcion_intregity,
                                excepcion_operational_error,
                                excepcion_peewee)


def listado_roles():
    return Usuario.select()


#nombre es unique asi que me sirve para buscar
def obtener_rol_por_nombre_usuario(nombre_usuario):
    return Rol.get_or_none(Rol.nombre == nombre_usuario)