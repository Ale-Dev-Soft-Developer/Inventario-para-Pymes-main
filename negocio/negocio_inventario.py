from datos.repositorios.repositorio_inventario import (guardar_inventario,
                                                       listado_inventario_almacen,
                                                       listado_inventario_general,
                                                       listado_inventario_producto,
                                                       listado_stock_critico,
                                                       obtener_inventario_por_id
                                                       )

from negocio.negocio_producto import obtener_producto
from negocio.negocio_almacen import obtener_almacen
from datos.repositorios.repositorio_inventario import Inventario


def asociar_producto_con_almacen(id_producto,id_almacen,stock_actual,stock_minimo):
        
    if obtener_producto(id_producto) is None:
        return False
    
    if obtener_almacen(id_almacen) is None:
        return False
    
    if stock_actual < 0 or stock_minimo < 0:
        return False
    
    if obtener_inventario_por_id(id_producto,id_almacen) is not None:
        return False
    
    
    asociar = Inventario()
    asociar.id_almacen = id_almacen
    asociar.id_producto = id_producto
    asociar.stock_minimo = stock_minimo
    asociar.stock_actual = stock_actual
    
    return guardar_inventario(asociar)


def obtener_listado_inventario_general():
    return listado_inventario_general()

def obtener_inventario_almacen():
    return listado_inventario_almacen()

def obtener_inventario_producto():
    return listado_inventario_producto()

def obtener_stock_critico():
    return listado_stock_critico()