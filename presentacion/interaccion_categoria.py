from datos.modelos.repositorios.repositorio_categoria import listado_categorias
from prettytable import PrettyTable

def listado_categorias():
    categorias = listado_categorias()
    tabla_paises = PrettyTable()
    tabla_paises.field_names = ["ID", "Nombre", "Descripción"]
    if categorias:
        for categoria in categorias:
            tabla_paises.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
    print(tabla_paises)