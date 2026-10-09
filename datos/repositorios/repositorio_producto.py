from datos.modelos.producto import Producto
from peewee import IntegrityError,OperationalError,DataError,PeeweeException
from auxiliares.mensajes import operacion_exitosa

#GET
def listado_productos():
    productos = Producto.select()
    if productos:
        return productos
    

#POST
def guardar_producto(producto:Producto):
    try:
        guardar = producto.save()
        print(guardar)
        return True
    
    except IntegrityError as e:
            print(f"Error al guardar Producto {producto.nombre}: {e}")
    except OperationalError as e:
            print(f"Error de operación: {e}")
    except DataError as e:
            print(f"Error de base de datos: {e}")
    except PeeweeException as e:
            print(f"Error de Peewee: {e}")
        
    return False


#PUT 
def actualizar_producto(producto:Producto):
    try:
        producto.save()
        return True
        
    except IntegrityError as e:
        print(f"Error al actualizar el Producto: {e}")
    except OperationalError as e:
        print(f"Error de operación: {e}")
    except DataError as e:
        print(f"Error de base de datos: {e}")
    except PeeweeException as e:
        print(f"Error de Peewee: {e}")
        
    return False


#DELETE
def borrado_logico_producto(producto:Producto):
    try: 
        producto.estado = False
        producto.save()
        return True
    
    except IntegrityError as e:
        print(f"Error al borrar el Producto: {e}")
    except OperationalError as e:
        print(f"Error de operación: {e}")
    except DataError as e:
        print(f"Error de base de datos: {e}")
    except PeeweeException as e:
        print(f"Error de Peewee: {e}")
        
    return False