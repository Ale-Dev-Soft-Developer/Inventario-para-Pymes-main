from datos.modelos.models import database
from datos.modelos.movimiento import Movimiento
from datos.repositorios.repositorio_movimiento import (guardar_movimiento,
                                                       listado_movimiento_generales,
                                                       listado_movimiento_entrada,
                                                       listado_movimiento_salida,
                                                       listado_movimientos_entre_fechas,
                                                       sumar_stock,
                                                       restar_stock)

from datos.repositorios.repositorio_inventario import (obtener_inventario)
from auxiliares.mensajes import (excepcion_peewee)
from peewee import PeeweeException


def obtener_movimientos_generales():
    return listado_movimiento_generales()

def obtener_movimientos_entrada():
    return listado_movimiento_entrada()

def obtener_movimiento_salida():
    return listado_movimiento_salida()

def obtener_movimientos_por_rangos_de_fecha(fecha_inicio,fecha_termino):
    return listado_movimientos_entre_fechas(fecha_inicio,fecha_termino)


def validar_stock_salida(id_categoria, cantidad):
    
    if cantidad <= 0:
        return False
    
    inventario = obtener_inventario(id_categoria)
    
    if inventario is None:
        return False
    
    if cantidad > inventario.stock_actual:
        return False
    
    return True


def registrar_entrada(cantidad,descripcion,fecha,id_inventario):
    
    if cantidad <= 0:
        return False
    
    try:
        
        with database.atomic():
            
            fila_actualizada = sumar_stock(id_inventario,cantidad)
            
            if fila_actualizada == 0:
                return False
            
            movimiento = Movimiento()
            movimiento.cantidad = cantidad
            movimiento.id_inventario = id_inventario
            movimiento.descripcion = descripcion
            movimiento.fecha = fecha
            movimiento.tipo = "ENTRADA"
            
            guardar_movimiento(movimiento)
            
            return True 
            
    except PeeweeException as e:
        print(PeeweeException(e))
        return False
    

def registrar_salida(cantidad,descripcion,fecha,id_inventario):
    
    if cantidad == 0:
        return False
    
    try:
        with database.atomic():
            
            fila_actualizada = restar_stock(id_inventario,cantidad)
            
            if fila_actualizada == 0:
                return False
            
            movimiento = Movimiento()
            movimiento.cantidad = cantidad
            movimiento.tipo = "SALIDA"
            movimiento.descripcion = descripcion
            movimiento.fecha = fecha
            
            guardar_movimiento(movimiento)
            return True
        
    except PeeweeException as e: 
        print(excepcion_peewee(e))