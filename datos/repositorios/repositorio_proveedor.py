from datos.modelos.proveedor import Proveedor
from peewee import IntegrityError,OperationalError,DataError,PeeweeException


#Metodo GET
def listado_proveedor():
    proveedor = Proveedor.select()
    if proveedor:
        return proveedor
    
    if not proveedor:
        return False
    

#POST
def guardar_proveedor(proveedor:Proveedor):
    try:
        return proveedor.save()
    
    except IntegrityError as e:
            print(f"Error al guardar Producto {proveedor.nombre}: {e}")
    except OperationalError as e:
            print(f"Error de operación: {e}")
    except DataError as e:
            print(f"Error de base de datos: {e}")
    except PeeweeException as e:
            print(f"Error de Peewee: {e}")
            
    return False


def obtener_proveedor_por_id(id_proveedor):
    return Proveedor.get_or_none(Proveedor.id_proveedor == id_proveedor)



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


#Comprobar rut,correo,telefono de un proveedor existe 
def existe_rut(rut, excluir_id=None):
    consulta = Proveedor.select().where(Proveedor.rut == rut)
    
    #Para excluir al mismo ID que hace la consulta
    if excluir_id is not None:
        consulta = consulta.where(Proveedor.id_proveedor != excluir_id)
        
    return consulta.exists()


def existe_correo(correo, excluir_id=None):
    #En la tabla de Proveedores Correo no es obligacion.
    if not correo:
        return False
    
    consulta = Proveedor.select().where(Proveedor.correo == correo)
    
    #Para excluir al mismo ID que hace la consulta
    if excluir_id is not None:
        consulta = consulta.where(Proveedor.id_proveedor != excluir_id)
        
    return consulta.exists()


def existe_telefono(telefono, excluir_id=None):
    consulta = Proveedor.select().where(Proveedor.telefono == telefono)
    
    #Para excluir al mismo ID que hace la consulta
    if excluir_id is not None:
        consulta = consulta.where(Proveedor.id_proveedor != excluir_id)
        
    return consulta.exists()