
from datos.modelos.movimiento import Movimiento
from datos.modelos.inventario import Inventario
from auxiliares.mensajes import (excepcion_peewee,
                                 excepcion_data_error,
                                 excepcion_operational_error,
                                 excepcion_intregity)
from peewee import (PeeweeException,
                    DataError,
                    OperationalError,
                    IntegrityError,
                    )


def movimientos_generales():
    return (Movimiento
            .select(Movimiento,Inventario)
            .join(Inventario)
            )


def listado_movimiento_generales():
    return movimientos_generales()


def listado_movimiento_entrada():
    return (movimientos_generales()
            .where(Movimiento.tipo == "ENTRADA"))


def listado_movimiento_salida():
    return (movimientos_generales()
            .where(Movimiento.tipo == "SALIDA"))


def listado_movimientos_entre_fechas(fecha_incio,fecha_termino):
    return (movimientos_generales()
            .where(Movimiento.fecha
            .between(fecha_incio,fecha_termino))
            )
 
    
#Como se usa un update, hay que utilizar la funcion excute()    
def sumar_stock(id_inventario,cantidad):
    return (Inventario
            .update(stock_actual = Inventario.stock_actual + cantidad)
            .where(Inventario.id_inventario == id_inventario)
            .execute()
            )
    

def restar_stock(id_inventario,cantidad):
    return (Inventario
            .update(stock_actual = Inventario.stock_actual - cantidad)
            .where((Inventario.id_inventario == id_inventario) & (Inventario.stock_actual >= cantidad))
            .execute()
            )


def guardar_movimiento(movimiento:Movimiento):
    
    try:
        
        movimiento.save()
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