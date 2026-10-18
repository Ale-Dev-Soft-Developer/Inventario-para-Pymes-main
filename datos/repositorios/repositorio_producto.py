from datos.modelos.producto import Producto

from datos.modelos.categoria import Categoria

from peewee import (IntegrityError,
                    OperationalError,
                    DataError,
                    PeeweeException)

from auxiliares.mensajes import (excepcion_peewee,
                                 excepcion_data_error,
                                 excepcion_operational_error,
                                 excepcion_intregity)

#GET
def listado_productos():
    productos = (Producto
                 .select(Producto,Categoria)
                 .join(Categoria))
    if productos:
        return productos
    return False
    

#POST
def guardar_producto(producto:Producto):
    try:
        
        producto.save()
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


#PUT 
def actualizar_producto(producto:Producto):
    
    try:
    
        producto.save()
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


#DELETE
def borrado_logico_producto(producto:Producto):
    
    try: 
    
        producto.estado = False
        producto.update()
    
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