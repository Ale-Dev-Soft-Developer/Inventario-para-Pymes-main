from peewee import (IntegrityError,
                    OperationalError,
                    DataError,
                    PeeweeException)
from datos.modelos.proveedor import Proveedor
from auxiliares.mensajes import (excepcion_data_error,
                                excepcion_intregity,
                                excepcion_operational_error,
                                excepcion_peewee)


#Metodo GET
def listado_proveedor():
    proveedor = Proveedor.select()
    if proveedor:
        return proveedor
    
    if not proveedor:
        return False
    

#POST AND UPDATE
def guardar_proveedor(proveedor:Proveedor):
    
    try:
        return proveedor.save()
    
    except IntegrityError as e:
            excepcion_intregity(e)
    except OperationalError as e:
            excepcion_operational_error(e)
    except DataError as e:
            excepcion_data_error(e)
    except PeeweeException as e:
            excepcion_peewee(e)
            
    return False


def obtener_proveedor_por_id(id_proveedor):
    return Proveedor.get_or_none(Proveedor.id_proveedor == id_proveedor)



#DELETE
def borrado_logico_proveedor(proveedor:Proveedor):
    try:
        proveedor.estado = False
        proveedor.save()
        return True
    
    except IntegrityError as e:
            excepcion_intregity(e)
    except OperationalError as e:
            excepcion_operational_error(e)
    except DataError as e:
            excepcion_data_error(e)
    except PeeweeException as e:
        excepcion_peewee(e)
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