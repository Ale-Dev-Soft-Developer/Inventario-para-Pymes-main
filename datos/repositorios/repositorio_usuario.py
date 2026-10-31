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

def listado_usuario():
    
    #Haciendo el JOIN con rol
    #para que al traer usuario salga el nombre del rol
    usuario = (Usuario
               .select(Usuario,Rol)
               .where(Usuario.estado == True)
               .join(Rol)
               .order_by(Usuario.nombre))
    
    if usuario:
        return usuario
    return False


def obtener_usuario_por_nombre(nombre_usuario):
    return Usuario.get_or_none(Usuario.usuario == nombre_usuario)


def guardar_usuario(usuario:Usuario):
    
    try:
        return usuario.save()
    
    except IntegrityError as e:
        excepcion_intregity(e)
    except OperationalError as e:
        excepcion_operational_error(e)
    except DataError as e:
        excepcion_data_error(e)
    except PeeweeException as e:
        excepcion_peewee(e)
    
    return False