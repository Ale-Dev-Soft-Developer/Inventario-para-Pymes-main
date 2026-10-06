from datos.modelos.repositorios.repositorio_categoria import listado_categorias,guardar_categoria
from datos.modelos.categoria import Categoria
from prettytable import PrettyTable

def listado_categorias():
    categorias = listado_categorias()
    tabla_categoria = PrettyTable()
    tabla_categoria.field_names = ["ID", "Nombre", "Descripción"]
    if categorias:
        for categoria in categorias:
            tabla_categoria.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
    print(tabla_categoria)
    
def guardar_categoria(nombre,descripion):
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripion
    guardar_categoria(nueva_categoria)