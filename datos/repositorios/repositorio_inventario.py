from datos.modelos.inventario import Inventario
from auxiliares.mensajes import (excepcion_peewee,
                                 excepcion_intregity,
                                 excepcion_operational_error,
                                 excepcion_data_error)
from peewee import (PeeweeException,
                    IntegrityError,
                    OperationalError,
                    DataError)

from datos.modelos.almacen import Almacen
from datos.modelos.producto import Producto


#este join hace una consulta en general de inventario.
#falta implementar y testear, aun en desarrollo.
def inventario_general():
    return (Inventario
            .select(Inventario,Producto,Almacen)
            .join(Producto)
            .switch(Inventario)
            .join(Almacen))

def listado_inventario_general():
    return inventario_general()


def listado_inventario_almacen(id_almacen):
    return inventario_general().where(Inventario.id_almacen == id_almacen)


def listado_inventario_producto(id_producto):
    return inventario_general().where(Inventario.id_producto == id_producto)


def listado_stock_critico():
    return (Inventario
            .select()
            .where(Inventario.stock_actual <= Inventario.stock_minimo))


#utilizar para validar relacion en negocio_inventario.
def obtener_inventario_por_id(id_inventario,id_producto):
    
    return Inventario.get_or_none(
        (Inventario.id_inventario == id_inventario)&
        (Inventario.id_producto == id_producto)
    )

def guardar_inventario(inventario:Inventario):
    
    try:
        inventario.save()
        return True
    
    except IntegrityError as e:
        print(excepcion_intregity(e))
    except OperationalError as e:
        print(excepcion_operational_error(e))
    except DataError as e:
        print(excepcion_data_error(e))
    except PeeweeException as e:
        print(excepcion_peewee(e))
    
    return False
