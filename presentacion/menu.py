from auxiliares import nombre_aplicacion,version_aplicacion
from auxiliares.menu import submenu_bodega,menu_superior, submenu_producto,submenu_categoria,submenu_proveedor
from auxiliares.mensajes import opcion_invalida,opcion_cancelada,solo_numeros_enteros,programa_finalizado,ingrese_id_categoria,ingrese_nombre_categoria,ingrese_descripcion_categoria
from negocio.negocio_categoria import listado_categorias,actualizar_categoria_existente
from presentacion.presentacion_categoria import solicitar_datos_categoria,actualizar_datos_categoria


#dejar mas expedito el menu principal, sin tantos bucles anidados. Ordenar el codigo.
def menu_principal():
    opcion = -1

    while opcion != 0:
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-7]: ').strip())
        except ValueError:
            print(solo_numeros_enteros)
            continue

        if opcion == 1:
            menu_categoria()
        elif opcion == 2:
            menu_producto()
        elif opcion == 3:
            menu_bodega()
        elif opcion == 4:
            menu_proveedor()
        elif opcion == 0:
            print(programa_finalizado)
        else:
            print(opcion_invalida)


def menu_categoria():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_categoria.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-2]: ').strip())
        except ValueError:
            print(solo_numeros_enteros)
            continue

        if opcion == 1:
            listado_categorias()
        elif opcion == 2:
            solicitar_datos_categoria()
        elif opcion == 3:
            listado_categorias()
            actualizar_datos_categoria()   
        elif opcion == 4:
            pass
        elif opcion != 0:
            print(opcion_invalida)


def menu_producto():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_producto.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-4]: ').strip())
        except ValueError:
            print(solo_numeros_enteros)
            continue

        if opcion == 1:
            pass
        elif opcion != 0:
            print(opcion_invalida)


def menu_bodega():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_bodega.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-4]: ').strip())
        except ValueError:
            print(solo_numeros_enteros)
            continue

        if opcion == 1:
            pass
        elif opcion != 0:
            print(opcion_invalida)


def menu_proveedor():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_proveedor.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-4]: ').strip())
        except ValueError:
            print(solo_numeros_enteros)
            continue

        if opcion == 1:
            pass
        elif opcion != 0:
            print(opcion_invalida)