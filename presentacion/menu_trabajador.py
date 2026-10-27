from auxiliares import (nombre_aplicacion,
                        version_aplicacion)

from auxiliares.menu import (submenu_bodega,
                             menu_superior,
                             submenu_producto,
                             submenu_categoria,
                             submenu_proveedor,
                             submenu_almacen)

from auxiliares.mensajes import (opcion_invalida,
                                 solo_numeros_enteros,
                                 programa_finalizado)


from presentacion.presentacion_categoria import (solicitar_datos_categoria,
                                                 actualizar_datos_categoria,
                                                 solicitar_desactivar_categoria,
                                                 listado_categorias)

from presentacion.presentacion_producto import (solicitar_datos_producto,
                                                actualizar_datos_producto,
                                                solicitar_desactivar_producto,
                                                listado_productos)

from presentacion.presentacion_proveedor import (mostrar_proveedores,
                                                 solicitar_datos_proveedor,
                                                 actualizar_datos_proveedor,
                                                 solicitar_desactivar_proveedor)


#dejar mas expedito el menu principal, sin tantos bucles anidados. Ordenar el codigo.
def menu_principal():
   
    opcion = -1

    while opcion != 0:
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-5]: ').strip())
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
        elif opcion == 5:
            menu_almacen()
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
            opcion = int(input('\nIngrese su opción [0-4]: ').strip())
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
            solicitar_datos_producto()
        elif opcion == 2:
            listado_productos()
            actualizar_datos_producto()
        elif opcion == 4:
            listado_productos()
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
            solicitar_datos_proveedor()
        elif opcion == 2:
            mostrar_proveedores()
            actualizar_datos_proveedor()
        elif opcion == 4:
            mostrar_proveedores()    
        elif opcion != 0:
            print(opcion_invalida)
            
            
            
def menu_almacen():
   
    opcion = -1

    while opcion != 0:
        
        for clave, valor in submenu_almacen.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-4]: ').strip())
        
        except ValueError:
            print(solo_numeros_enteros)
            continue

        if opcion == 1:
            solicitar_datos_proveedor()
        elif opcion == 2:
            actualizar_datos_proveedor()
        elif opcion == 4:
            mostrar_proveedores()    
        elif opcion != 0:
            print(opcion_invalida)