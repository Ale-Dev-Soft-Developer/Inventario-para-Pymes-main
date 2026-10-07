from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationError, DataError, PeeweeException

def listado_categorias():
    categorias = Categoria.select()
    if categorias:
        return categorias
    
    # categoria:Categoria con esto le digo que la variable categoria es de tipo Categoria. 
    # va a la clase Categoria y me crea el objeto categoria con los atributos de la clase Categoria.
def guardar_categoria(categoria:Categoria):
    try: 
        guardar = categoria.save() #cambie el nombre por repetecion de variable "guardar_categoria"
        print(f"{guardar}")
    except IntegrityError as e:
        print(f"Error al guardar la categoría: {e}")
    except OperationError as e:
        print(f"Error de operación: {e}")
    except DataError as e:
        print(f"Error de base de datos: {e}")
    except PeeweeException as e:
        print(f"Error de Peewee: {e}")
        
def actualizar_categoria(categoria:Categoria):
    try:
        categoria.save()
        print(f"Se ha actualizado {categoria.nombre}")
    except IntegrityError as e:
        print(f"Error al actualizar la categoría: {e}")
    except OperationError as e:
        print(f"Error de operación: {e}")
    except DataError as e:
        print(f"Error de base de datos: {e}")
    except PeeweeException as e:
        print(f"Error de Peewee: {e}")