from datos.modelos.repositorios.repositorio_categoria import listado_categorias,guardar_categoria,actualizar_categoria
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
    
def crear_categoria(nombre,descripion): #cambio de nombre de la funcion para no confundir con la otra funcion "guardar_categoria"
    nueva_categoria = guardar_categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripion
    guardar_categoria(nueva_categoria)
    
def actualizar_categoria_existente(nombre,descripcion):
    
    actualizar_categoria_existente = actualizar_categoria()
    
    actualizar_categoria_existente.nombre = nombre
    actualizar_categoria_existente.descripcion = descripcion
    
    actualizar_categoria(actualizar_categoria)