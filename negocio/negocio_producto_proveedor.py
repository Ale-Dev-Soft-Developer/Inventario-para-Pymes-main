from datos.repositorios.repositorio_producto_proveedor import (crear_relacion_producto_proveedor,
                                                               obtener_proveedor_principal,
                                                               obtener_relacion_producto_proveedor,
                                                               borrado_fisico_relacion,
                                                               listado_proveedores_asociados,
                                                               listado_proveedor_producto
                                                               )

from negocio.negocio_producto import obtener_producto
from negocio.negocio_proveedor import obtener_proveedor
from datos.repositorios.repositorio_producto_proveedor import ProductoProveedor
from datos.modelos.proveedor import Proveedor


def listado_proveedores_asociados():
    return listado_proveedores_asociados()

def lista_proveedores_producto(id_producto):
    return listado_proveedor_producto(id_producto)

def proveedor_principal(id_producto):
    return obtener_proveedor_principal(id_producto)


def asignar_proveedor_principal(id_producto, id_proveedor):
    
    
    producto = obtener_producto(id_producto)
    proveedor = obtener_proveedor(id_proveedor)

    if producto is None or proveedor is None:
        return False

    if obtener_proveedor_principal(id_producto) is not None:
        return False

    return (crear_relacion_producto_proveedor(id_producto, id_proveedor, es_principal=True)) 


def asignar_proveedor_secundario(id_producto, id_proveedor):
    
    producto = obtener_producto(id_producto)
    proveedor = obtener_proveedor(id_proveedor)

    if producto is None or proveedor is None:
        return False

    relacion = obtener_relacion_producto_proveedor(id_producto, id_proveedor)
    
    if relacion is not None:
        return False
    
    return crear_relacion_producto_proveedor(id_producto, id_proveedor, es_principal=False)


def eliminar_relacion(id_producto, id_proveedor):
    
    relacion = obtener_relacion_producto_proveedor(id_producto, id_proveedor)

    if relacion is None:
        return False
    
    return borrado_fisico_relacion(relacion)