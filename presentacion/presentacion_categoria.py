from negocio.negocio_categoria import (actualizar_categoria_existente,
                                       crear_categoria,
                                       listado_categoria,
                                       desactivar_categoria,
                                       activar_categoria,
                                       listar_categorias_desactivadas)

from auxiliares.entradas import (forzar_entero,
                                 campo_obligatorio,
                                 campo_opcional)

from auxiliares.mensajes import (no_existe_categoria,
                                 OPCION_INVALIDA)

from prettytable import PrettyTable



def solicitar_seleccion_categoria():
    categorias = listado_categoria()

    if not categorias:
        print(no_existe_categoria)
        return None

    print("\nCategorias disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"[{i}] - {categoria.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione la categoria: ")

        if 1 <= seleccion <= len(categorias):
            opcion_valida = True
            return categorias[seleccion - 1]

        print(f"Opcion fuera de rango (1-{len(categorias)}).")


def listado_categorias():
    
    categorias = listado_categoria()
    
    if not categorias:
        print(no_existe_categoria)
        return None
    
    tabla_categoria = PrettyTable()
    tabla_categoria.field_names = ["ID", "Nombre", "Descripción","Estado"]
    
        
    for categoria in categorias:
        tabla_categoria.add_row([categoria.id_categoria,
                                     categoria.nombre,
                                     categoria.descripcion,
                                     ('Inhabilitado', 'Habilitado')[categoria.estado]
                                     ])
        print(tabla_categoria)



def solicitar_datos_categoria():
    
    print("\n=== Registrar Categoria ===")
    nombre = campo_obligatorio("Ingrese el nombre de la categoria: ")
    descripcion = campo_obligatorio("Ingrese la descripion de la categoria: ")
        
    resultado = crear_categoria(nombre, descripcion)
    print("Categoria creada con exito.") if resultado else print("No se pudo crear la categoria.")
        

def solicitar_consultar_categoria():
    
    categoria = solicitar_seleccion_categoria()

    if categoria is None:
        return 

    estado = "Habilitado" if categoria.estado else "Deshabilitado" #Ternario

    print("\n=== Informacion Categoria ===")
    print(f"{'ID':<16}: {categoria.id_categoria}")
    print(f"{'Nombre':<16}: {categoria.nombre}")
    print(f"{'Descripcion':<16}: {categoria.descripcion}")
    print(f"{'Estado':<16}: {estado}\n")

            
def actualizar_datos_categoria():
    
    categoria = solicitar_seleccion_categoria()

    if categoria is None:
        return 
    
    nombre = campo_opcional("Ingrese el nuevo nombre", categoria.nombre)   
    descripcion = campo_opcional("Ingrese la nueva descripion", categoria.descripcion)

    resultado = actualizar_categoria_existente(categoria, nombre, descripcion)
    print("Categoria actualizada con exito.") if resultado else print("No se pudo actualizar la categoria.") #Ternario
        

def solicitar_desactivar_categoria():
    categoria = solicitar_seleccion_categoria()

    if categoria is None:
        return 

    confirmar = input(f"Estas seguro de desactivar la categoria: {categoria.nombre}? (S/N): ").strip().upper()
    if confirmar == "S":
        resultado = desactivar_categoria(categoria)
        print(f"Categoria: {categoria.nombre} desactivada con exito.") if resultado else print("No se pudo desactivar la categoria.") 
    elif confirmar == "N":
        print("Opcion Cancelada.")
    else:
        print(OPCION_INVALIDA)
        

def solicitar_activar_categoria():
    
    categorias = listar_categorias_desactivadas() # Lista de objetos

    if not categorias:
        print("No hay categorias desactivadas.")
        return None

    print("\nCategorias Desactivadas:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"[{i}] - {categoria.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione la categoria: ")

        if 1 <= seleccion <= len(categorias):
            opcion_valida = True
            categoria = categorias[seleccion - 1] # Objeto Categoria
        else:
            print(f"Opcion fuera de rango (1-{len(categorias)}).")    

    if categoria is None:
        return 

    resultado = activar_categoria(categoria)
    print(f"Categoria: {categoria.nombre} activada con exito.") if resultado else print("No se pudo activar la categoria.") 