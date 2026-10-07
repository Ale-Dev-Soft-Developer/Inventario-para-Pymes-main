from negocio.negocio_categoria import listado_categorias, crear_categoria, actualizar_categoria_existente


def solicitar_datos_categoria():
    
    nombre = descripcion = ""
    
    while nombre == "":
        nombre = input("Ingrese el nombre de la categoria: ")
    while descripcion == "":    
        descripcion = input("Ingrese la descripion de la categoria: ")
    
    crear_categoria(nombre,descripcion)
    

def actualizar_datos_categoria():
    nombre = descripcion = ""
        
    while nombre == "":
        nombre = input("Ingrese el nombre de la categoria: ")
    while descripcion == "":    
        descripcion = input("Ingrese la descripion de la categoria: ")
        
    actualizar_categoria_existente(nombre,descripcion)
        

def eliminar_datos_categoria():
    pass