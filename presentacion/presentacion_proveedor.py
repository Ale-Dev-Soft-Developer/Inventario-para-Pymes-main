from negocio.negocio_proveedor import(listado_proveedor,
                                      crear_proveedor,
                                      actualizar_proveedor_existente,
                                      actualizar_direccion_existente,
                                      desactivar_proveedor,
                                      obtener_proveedor,
                                      existe_correo,
                                      validar_rut,
                                      existe_telefono)
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
                                 ingrese_numero_proveedor,
                                 ingrese_ID_buscar,
                                 solo_numeros_enteros,
                                 producto_por_id_no_existe,
                                 titulo_actualizar_proveedor,
                                 rut_existente,
                                 rut_invalido,
                                 no_existe_proveedor,
                                 operacion_exitosa,
                                 ingrese_id_proveedor,
                                 confirmar_borrar_proveedor,
                                 no_se_concreto_la_operacion)
from auxiliares.entradas import (desea_modificar,pedir_entero)
from prettytable import PrettyTable
from datos.modelos.proveedor import Proveedor


def mostrar_proveedores():
    
    proveedores = listado_proveedor()

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    tabla_proveedores = PrettyTable()
    tabla_proveedores.field_names = ['Id', 'Rut', 'Nombre', 'Correo', 'Telefono', 'Estado', 'Id Direccion']

    for proveedor in proveedores:
        tabla_proveedores.add_row([
            proveedor.id_proveedor,
            proveedor.rut,
            proveedor.nombre,
            proveedor.correo,
            proveedor.telefono,
            ('Deshabilitado', 'Habilitado')[proveedor.estado], #Ternario
            proveedor.id_direccion,
        ])

    print(tabla_proveedores)


def solicitar_datos_proveedor():
    
    rut = pedir_texto(ingrese_rut_proveedor)
    
    if not validar_rut(rut):
        print(rut_invalido)
    
    nombre = pedir_texto(ingrese_nombre_proveedor)
    correo = pedir_texto(ingrese_correo_proveedor)
    
    if existe_correo(correo):
        return False
    
    telefono = pedir_texto(ingrese_telefono_proveedor)
    
    if existe_telefono(telefono):
        return False
    
    
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
    
    #Muestro proveedores con su ID
    listado_proveedor()
    
    try: 
        id_proveedor = int(input(ingrese_ID_buscar))
    except ValueError:
        print(solo_numeros_enteros)
        return
    
    proveedor = obtener_proveedor(id_proveedor)
    
    if proveedor is None:
        print(producto_por_id_no_existe)
        return
    
    print(titulo_actualizar_proveedor(id_proveedor))
    
    #Campo por campo que necesita actualizar
    nombre = proveedor.nombre
    if desea_modificar("el nombre: ", nombre):
        nombre = pedir_texto(ingrese_nombre_proveedor)
    
    telefono = proveedor.telefono
    if desea_modificar("el numero telefonico: ",telefono):
        telefono = pedir_texto(ingrese_telefono_proveedor)
        
    correo = proveedor.correo
    if desea_modificar("el correo electronico: ",correo):
        correo = pedir_texto(ingrese_correo_proveedor)
        
    comuna = proveedor.comuna
    if desea_modificar("la comuna: ", comuna):
        comuna = pedir_texto(ingrese_comuna_proveedor)
        
    ciudad = proveedor.ciudad
    if desea_modificar("la ciudad: ", ciudad):
        ciudad = pedir_texto(ingrese_ciudad_proveedor)
        
    calle = proveedor.calle
    if desea_modificar("la calle : ",calle):
        pedir_texto(ingrese_calle_proveedor)
        
    numero = proveedor.numero
    if desea_modificar("el numero de su casa o Dpto: ", numero):
        pedir_texto(ingrese_numero_proveedor)
        
    return (
        actualizar_proveedor_existente(id_proveedor,nombre,telefono,correo),
        actualizar_direccion_existente(id_proveedor,ciudad,comuna,calle,numero)
        )
    


#DELETE
def solicitar_desactivar_proveedor():
    
    listado_proveedor()
    
    #Validacion interna desde auxiliares/entradas.py
    id_proveedor = input(pedir_entero(ingrese_id_proveedor))
    
    proveedor_instancia = Proveedor()
    
    proveedor = obtener_proveedor(id_proveedor)
    if proveedor is None:
        print(no_existe_proveedor)
        
    
    confirmar = input(pedir_confirmacion(confirmar_borrar_proveedor))
        
    if confirmar == "s":
        
        desactivar_proveedor(id_proveedor)
        
        #Validacion para asegurarse que el estado haya sido modificado.
        if proveedor_instancia.estado is False:
                print(operacion_exitosa)
        else:
            print(no_se_concreto_la_operacion)
    
   
    
    
    
        