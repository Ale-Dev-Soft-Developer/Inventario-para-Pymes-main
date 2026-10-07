from datos.repositorios.repositorio_categoria import listado_categorias,guardar_categoria,actualizar_categoria
from datos.modelos.categoria import Categoria
from prettytable import PrettyTable


def listado_categorias():
    
    tabla_categoria = PrettyTable()
    tabla_categoria.field_names = ["ID", "Nombre", "Descripción"]
    
    data_de_categorias = listado_categorias() #instancia para revisar la data de la tabla
    
    if data_de_categorias:
        
        for categoria in data_de_categorias:
            tabla_categoria.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
        print(tabla_categoria)
    
    if not data_de_categorias:
        print("No hay ninguna Categoria registrada")

    
def crear_categoria(nombre,descripion): 
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripion
    guardar_categoria(nueva_categoria)


def obtener_categoria(id_categoria):
    
    try: 
        return Categoria[id_categoria]
    except Categoria.DoesNotExist:
        return None
    
def actualizar_categoria_existente(id_categoria,nombre,descripcion):
    
    categoria = obtener_categoria(id_categoria)
    
    if categoria == None:
        return False
    
    
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    
    actualizar_categoria(categoria)
    
# Metodo para Eliminar Categoria (borrado logico)
def desactivar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    # estado es un booleano, solo necesito cambiarlo a False para desactivarlo
    categoria.estado = False
    return guardar_categoria(categoria)

# Metodo para activar Categoria
def activar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    categoria.estado = True
    return guardar_categoria(categoria)