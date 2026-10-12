from datos.modelos.proveedor import Proveedor
from peewee import IntegrityError,OperationalError,DataError,PeeweeException


#Metodo GET
def listado_proveedor():
    proveedor = Proveedor.select()
    if proveedor:
        return proveedor
    

#POST
def guardar_proveedor(proveedor:Proveedor):
    try:
        guardar = proveedor.save()
        print(guardar)
        return True
    
    except IntegrityError as e:
            print(f"Error al guardar Producto {proveedor.nombre}: {e}")
    except OperationalError as e:
            print(f"Error de operación: {e}")
    except DataError as e:
            print(f"Error de base de datos: {e}")
    except PeeweeException as e:
            print(f"Error de Peewee: {e}")
            
    return False


#UPDATE
def actualizar_proveedor(proveedor:Proveedor):
    try:
        proveedor.update()
        return True
    
    except IntegrityError as e:
            print(f"Error al guardar Producto {proveedor.nombre}: {e}")
    except OperationalError as e:
            print(f"Error de operación: {e}")
    except DataError as e:
            print(f"Error de base de datos: {e}")
    except PeeweeException as e:
            print(f"Error de Peewee: {e}")
            
    return False


#DELETE
def borrado_logico_proveedor(proveedor:Proveedor):
    try:
        proveedor.estado = False
        proveedor.update()
        return True
    
    except IntegrityError as e:
            print(f"Error al guardar Producto {proveedor.nombre}: {e}")
    except OperationalError as e:
            print(f"Error de operación: {e}")
    except DataError as e:
            print(f"Error de base de datos: {e}")
    except PeeweeException as e:
            print(f"Error de Peewee: {e}")
            
    return False


#Comprobar rut de un proveedor existe y "(&)" que este activo.
def existe_rut(rut):
    return Proveedor.select().where(
        (Proveedor.rut == rut) &
        (Proveedor.estado == 1)
    ).exists()