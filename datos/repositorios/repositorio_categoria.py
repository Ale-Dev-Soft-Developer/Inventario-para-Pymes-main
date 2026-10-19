from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationalError, DataError, PeeweeException
from auxiliares.mensajes import (excepcion_peewee,
                                 excepcion_data_error,
                                 excepcion_operational_error,
                                 excepcion_intregity)

#GET 
def listado_categorias():
    
    categorias = Categoria.select().where(Categoria.estado == True) #para ocultar las de borrado logico
    
    if categorias:
        return categorias
    return False
    

def obtener_categoria_por_id(id_categoria):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria) 


#POST_AND_UPDATE
def guardar_categoria(categoria:Categoria):
    try: 
        guardar = categoria.save()
        print(f"{guardar}")
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