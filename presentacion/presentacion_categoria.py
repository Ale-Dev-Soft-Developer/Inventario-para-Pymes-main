from negocio.negocio_categoria import actualizar_categoria_existente, crear_categoria, obtener_categoria,desactivar_categoria,activar_categoria
from auxiliares.mensajes import ingrese_descripcion_categoria,ingrese_nombre_categoria,confirmar_borrar_categoria,categoria_borrada_exito,categoria_no_borrada,ingrese_id_categoria,opcion_cancelada,opcion_invalida,categoria_no_existe,id_debe_ser_entero

def solicitar_datos_categoria():
    
    nombre = descripcion = ""
    
    while nombre == "":
        nombre = input(f"{ingrese_nombre_categoria}")
    while descripcion == "":    
        descripcion = input(f"{ingrese_descripcion_categoria}")
    
    return crear_categoria(nombre,descripcion)
    

def actualizar_datos_categoria():
    
    try:
        id_categoria = int(input(ingrese_id_categoria))
    except ValueError:
        print(id_debe_ser_entero)
        return

    # Buscamos la categoria por su ID
    # Si existe, obtenemos el objeto Categoria y si no existe obtenemos None
    categoria = obtener_categoria(id_categoria)

    # Si no encontro la categoria se detiene la funcion actual
    if categoria is None:
        print(categoria_no_existe)
        return 

    nombre = descripcion = ""
        
    while nombre == "":
        nombre = input(f"{ingrese_nombre_categoria}")
    while descripcion == "":    
        descripcion = input(f"{ingrese_descripcion_categoria}")

    return actualizar_categoria_existente(id_categoria, nombre, descripcion) 
        

def solicitar_desactivar_categoria():
    try:
        id_categoria = int(input(ingrese_id_categoria))
    except ValueError:
        print(id_debe_ser_entero)
        return

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(categoria_no_existe)
        return 

    confirmar = input(confirmar_borrar_categoria({confirmar})).strip().upper()
    if confirmar == "S":
        resultado = desactivar_categoria(id_categoria)
        if resultado:
            print(categoria_borrada_exito(categoria))
        else:
            print(categoria_no_borrada)
    elif confirmar == "N":
        print(opcion_cancelada)
    else:
        print(opcion_invalida) 


def solicitar_activar_categoria():
    try:
        id_categoria = int(input(ingrese_id_categoria))
    except ValueError:
        print(id_debe_ser_entero)
        return

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(categoria_no_existe)
        return 

    return activar_categoria(id_categoria)