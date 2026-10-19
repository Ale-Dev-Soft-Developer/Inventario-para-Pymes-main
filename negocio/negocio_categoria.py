from datos.repositorios.repositorio_categoria import (listado_categorias as obtener_listado_categoria,
                                                      guardar_categoria,
                                                      obtener_categoria_por_id)
from datos.modelos.categoria import Categoria


#GET
def listado_categoria():
    return obtener_listado_categoria()


#GET_FOR_ID
def obtener_categoria(id_categoria):
    return obtener_categoria_por_id(id_categoria)


#POST    
def crear_categoria(nombre,descripcion): 
    
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    
    return guardar_categoria(nueva_categoria)


#UPDATE_FOR_ID    
def actualizar_categoria_existente(id_categoria,nombre,descripcion):
    
    categoria = obtener_categoria(id_categoria)
    
    if categoria is None:
        return False
    
    
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    
    return guardar_categoria(categoria)


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