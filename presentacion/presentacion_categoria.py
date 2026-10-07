from negocio.negocio_categoria import listado_categorias, guardar_categoria, solicitar_datos_categoria

def solicitar_datos_categoria():
    descripcion = input("Ingrese la descripción de la categoría: ")
    nombre = input("Ingrese el nombre de la categoría: ")
    return nombre, descripcion

def actualizar_datos_categoria():
    nombre = input("Ingrese el nuevo nombre de la categoría: ")
    descripcion = input("Ingrese la nueva descripción de la categoría: ")
    return nombre, descripcion

def eliminar_datos_categoria():
    pass