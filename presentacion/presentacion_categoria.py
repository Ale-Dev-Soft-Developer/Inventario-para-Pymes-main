from negocio.negocio_categoria import (actualizar_categoria_existente,
                                       crear_categoria,
                                       listado_categoria,
                                       desactivar_categoria,
                                       obtener_categoria)

from auxiliares.entradas import (pedir_entero,pedir_confirmacion)

from auxiliares.mensajes import (ingrese_descripcion_categoria,
                                 ingrese_nombre_categoria,
                                 confirmar_borrar_categoria,
                                 ingrese_id_categoria,
                                 opcion_cancelada,
                                 opcion_invalida,
                                 id_debe_ser_entero,
                                 no_existe,
                                 ingresaras_lo_siguiente,
                                 estas_seguro,
                                 no_existe_registro,
                                 operacion_exitosa,
                                 no_se_concreto_la_operacion)

from prettytable import PrettyTable
from datos.modelos.categoria import Categoria

def listado_categorias():
    
    categorias = listado_categoria()
    
    if not categorias:
        print(no_existe_registro(Categoria))
    
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
    
    nombre = descripcion = ""
    
    while nombre == "":
        nombre = input(f"{ingrese_nombre_categoria}")
    while descripcion == "":    
        try:
            descripcion = input(f"{ingrese_descripcion_categoria}")
    
            print(ingresaras_lo_siguiente(nombre,descripcion))
        
            confirmacion = input(estas_seguro).lower()
            if confirmacion == 's':
                return crear_categoria(nombre,descripcion)
            elif confirmacion == 'n':
                print(opcion_cancelada)
            else:
                print(opcion_invalida)
        except ValueError:
            print(opcion_invalida)
    

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
        print(no_existe(categoria))
        return 

    nombre = descripcion = ""
        
    while nombre == "":
        nombre = input(f"{ingrese_nombre_categoria}")
    while descripcion == "":    
        descripcion = input(f"{ingrese_descripcion_categoria}")

    return actualizar_categoria_existente(id_categoria, nombre, descripcion) 
        

def solicitar_desactivar_categoria():
    
    #validacion interna de que sea entero.
    id_categoria = input(pedir_entero(ingrese_id_categoria))
    
    categoria_instancia = Categoria()

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(no_existe(categoria)) 

    confirmar = input(pedir_confirmacion(confirmar_borrar_categoria))
    
    if confirmar == "s":

        desactivar_categoria(id_categoria)
        
        if categoria_instancia.estado is False:
            print(operacion_exitosa)
        else:
            print(no_se_concreto_la_operacion)