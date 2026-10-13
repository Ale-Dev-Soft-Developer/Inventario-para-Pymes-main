from negocio.negocio_proveedor import(listado_proveedor,
                                      crear_proveedor,
                                      actualizar_proveedor_existente,
                                      actualizar_direccion_existente,
                                      desactivar_proveedor)
from auxiliares.entradas import (pedir_texto,pedir_confirmacion)
from auxiliares.mensajes import (ingrese_nombre_proveedor,
                                 ingrese_rut_proveedor,
                                 ingrese_telefono_proveedor,
                                 ingrese_correo_proveedor,
                                 estas_seguro,
                                 opcion_cancelada,
                                 ingrese_calle_proveedor,
                                 ingrese_ciudad_proveedor,
                                 ingrese_comuna_proveedor,
                                 ingrese_numero_proveedor)


def solicitar_datos_proveedor():
    
    nombre = pedir_texto(ingrese_nombre_proveedor)
    rut = pedir_texto(ingrese_rut_proveedor)
    telefono = pedir_texto(ingrese_telefono_proveedor)
    correo = pedir_texto(ingrese_correo_proveedor)
    comuna = pedir_texto(ingrese_comuna_proveedor)
    ciudad = pedir_texto(ingrese_ciudad_proveedor)
    calle = pedir_texto(ingrese_calle_proveedor)
    numero = pedir_texto(ingrese_numero_proveedor)
    
    
    if not pedir_confirmacion(estas_seguro):
        print(opcion_cancelada)
        return None
    
    return crear_proveedor(
        nombre = nombre,
        rut = rut,
        telefono = telefono,
        correo = correo,
        comuna = comuna,
        ciudad = ciudad,
        calle = calle,
        numero = numero
    )
    

def actualizar_datos_proveedor():
    pass