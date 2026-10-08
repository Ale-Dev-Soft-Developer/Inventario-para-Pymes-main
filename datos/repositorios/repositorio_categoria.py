from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

#GET 
def listado_categorias():
    categorias = Categoria.select().where(Categoria.estado == True) #para ocultar las de borrado logico
    if categorias:
        return categorias
    

#POST
def guardar_categoria(categoria:Categoria):
    try: 
        guardar = categoria.save()
        print(f"{guardar}")
        return True
        
    except IntegrityError as e:
        print(f"Error al guardar la categoría: {e}")
    except OperationalError as e:
        print(f"Error de operación: {e}")
    except DataError as e:
        print(f"Error de base de datos: {e}")
    except PeeweeException as e:
        print(f"Error de Peewee: {e}")
    
    return False

#PUT o CATCH        
def actualizar_categoria(categoria:Categoria):
    try:
        categoria.save()
        print("Se ha actualizado")
        return True
    
    except IntegrityError as e:
        print(f"Error al actualizar la categoría: {e}")
    except OperationalError as e:
        print(f"Error de operación: {e}")
    except DataError as e:
        print(f"Error de base de datos: {e}")
    except PeeweeException as e:
        print(f"Error de Peewee: {e}")
    
    return False
        
#DELETE
def borrado_logico_categoria(categoria:Categoria):
    try:
            categoria.estado = False
            categoria.save()
            return True
        
    except IntegrityError as e:
            print(f"Error al actualizar la categoría: {e}")
    except OperationalError as e:
            print(f"Error de operación: {e}")
    except DataError as e:
            print(f"Error de base de datos: {e}")
    except PeeweeException as e:
            print(f"Error de Peewee: {e}")
        
    return False