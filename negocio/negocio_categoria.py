from datos.repositorios.repositorio_categoria import listado_categorias as obtener_listado_categoria,guardar_categoria,actualizar_categoria,borrado_logico_categoria
from datos.modelos.categoria import Categoria
from prettytable import PrettyTable
from auxiliares.mensajes import no_existe

#GET
def listado_categorias():
    
    tabla_categoria = PrettyTable()
    tabla_categoria.field_names = ["ID", "Nombre", "Descripción"]
    
    data_de_categorias = obtener_listado_categoria() #instancia para revisar la data de la tabla
    
    if data_de_categorias:
        
        for categoria in data_de_categorias:
            tabla_categoria.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
        print(tabla_categoria)
    
    if not data_de_categorias:
        print(no_existe(data_de_categorias))

#POST    
def crear_categoria(nombre,descripcion): 
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    guardar_categoria(nueva_categoria)


#GET_FOR_ID
def obtener_categoria(id_categoria):
    
    try: 
        return Categoria[id_categoria]
    except Categoria.DoesNotExist:
        return None

#UPDATE_FOR_ID    
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
    return borrado_logico_categoria(categoria)

# Metodo para activar Categoria
def activar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    categoria.estado = True
    return guardar_categoria(categoria)