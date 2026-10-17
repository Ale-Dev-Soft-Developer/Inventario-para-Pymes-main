from datos.modelos.productoProveedor import ProductoProveedor
from datos.modelos.proveedor import Proveedor

from auxiliares.mensajes import (excepcion_intregity,
                                 excepcion_peewee)

from peewee import (IntegrityError,
                    PeeweeException)

def listado_proveedores_asociados():
    return ProductoProveedor.select()


def listado_proveedor_producto(id_producto):
    
    return (ProductoProveedor
            .select(ProductoProveedor,Proveedor)
            .join(Proveedor)
            .where(ProductoProveedor.id_producto == id_producto))


def crear_relacion_producto_proveedor(id_producto, id_proveedor, es_principal=False):
    
    try:
        
        ProductoProveedor.create(
            id_producto=id_producto,
            id_proveedor=id_proveedor,
            es_principal=es_principal,
        )
        return True
    
    except IntegrityError as e:
        print(excepcion_intregity(e))
    except PeeweeException as e:
        print(excepcion_peewee(e))
    
    return False

def obtener_relacion_producto_proveedor(id_producto, id_proveedor):
    
    return ProductoProveedor.get_or_none(
        (ProductoProveedor.id_producto == id_producto) &
        (ProductoProveedor.id_proveedor == id_proveedor)
    )
    


def obtener_proveedor_principal(id_producto):
    return ProductoProveedor.get_or_none(
        (ProductoProveedor.id_producto == id_producto)
        & (ProductoProveedor.es_principal == True))
    

def borrado_fisico_relacion(relacion):
    
    try:
        return relacion.delete_instance() 
    
    except PeeweeException as e:
        print(excepcion_peewee(e))
    
    return False 