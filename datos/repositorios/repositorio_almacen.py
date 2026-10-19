from datos.modelos.almacen import Almacen
from peewee import IntegrityError,OperationalError,DataError,PeeweeException
from auxiliares.mensajes import (excepcion_data_error,
                                excepcion_intregity,
                                excepcion_operational_error,
                                excepcion_peewee)


def listado_almacen():
    
    almacen = (Almacen
               .select()
               .where(Almacen.estado == True)
               )
    
    if almacen:
        return almacen
    
    if not almacen:
        return False
    
def obtener_almacen_por_id(id_almecen):
    return Almacen.get_or_none(Almacen.id_almacen == id_almecen)
    

def guardar_almacen(almacen:Almacen):
    
    try:
        return almacen.save()
    
    except IntegrityError as e:
        excepcion_intregity(e)
    except OperationalError as e:
        excepcion_operational_error(e)
    except DataError as e:
        excepcion_data_error(e)
    except PeeweeException as e:
        excepcion_peewee(e)
    
    return False