from negocio.negocio_categoria import actualizar_categoria_existente, crear_categoria, obtener_categoria,desactivar_categoria,activar_categoria


def solicitar_datos_categoria():
    
    nombre = descripcion = ""
    
    while nombre == "":
        nombre = input("Ingrese el nombre de la categoria: ")
    while descripcion == "":    
        descripcion = input("Ingrese la descripion de la categoria: ")
    
    return crear_categoria(nombre,descripcion)
    

def actualizar_datos_categoria():
    
    try:
        id_categoria = int(input("Ingrese el ID de la categoria: "))
    except ValueError:
        print("El ID debe ser un numero entero.")
        return

    # Buscamos la categoria por su ID
    # Si existe, obtenemos el objeto Categoria y si no existe obtenemos None
    categoria = obtener_categoria(id_categoria)

    # Si no encontro la categoria se detiene la funcion actual
    if categoria is None:
        print("No existe una categoría con ese ID.")
        return 

    nombre = input("Ingrese el nombre de la categoria: ")   
    descripcion = input("Ingrese la descripion de la categoria: ")

    return actualizar_categoria_existente(id_categoria, nombre, descripcion) 
        

def solicitar_desactivar_categoria():
    try:
        id_categoria = int(input("Ingrese el ID de la categoria: "))
    except ValueError:
        print("El ID debe ser un numero entero.")
        return

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print("No existe una categoría con el ID ingresado.")
        return 

    confirmar = input(f"Estas seguro de desactivar la categoria: {categoria.nombre}? (S/N): ").strip().upper()
    if confirmar == "S":
        resultado = desactivar_categoria(id_categoria)
        if resultado:
            print(f"Categoria '{categoria.nombre}' desactivada con exito.")
        else:
            print("No se pudo desactivar la categoría.")
    elif confirmar == "N":
        print("Opcion Cancelada.")
    else:
        print("Opcion invalida.") 

def solicitar_activar_categoria():
    try:
        id_categoria = int(input("Ingrese el ID de la categoria: "))
    except ValueError:
        print("El ID debe ser un numero entero.")
        return

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print("No existe una categoria con el ID ingresado.")
        return 

    return activar_categoria(id_categoria)