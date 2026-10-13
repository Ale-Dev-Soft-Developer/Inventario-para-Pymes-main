from datos.repositorios.repositorio_proveedor import( listado_proveedor as obtener_listado_proveedor,
                                                     actualizar_proveedor,
                                                     guardar_proveedor,
                                                     borrado_logico_proveedor,
                                                     existe_rut,
                                                     existe_correo,
                                                     existe_telefono,
                                                     
                                                    )
from negocio.negocio_direccion import (crear_direccion,actualizar_direccion)
from datos.repositorios.repositorio_direccion import guardar_direcciones
from datos.modelos.proveedor import Proveedor
from prettytable import PrettyTable
from auxiliares.mensajes import no_existe

#GET
def listado_proveedor():
    tabla_proveedor = PrettyTable()
    tabla_proveedor.field_names = ["ID","Nombre","Rut","Correo","Telefono","Direccion","Estado"]
    
    data_de_proveedor = obtener_listado_proveedor()
    
    if data_de_proveedor:
        for proveedor in data_de_proveedor:
            tabla_proveedor.add_row([
                proveedor.id_proveedor,
                proveedor.nombre,
                proveedor.rut,
                proveedor.correo,
                proveedor.telefono,
                proveedor.id_direccion,
                proveedor.estado
            ])
            print(data_de_proveedor)
            
    if not data_de_proveedor:
        print(no_existe(data_de_proveedor))
        

#Validacion de Rut
def validar_rut(rut):
    
    #strip para evitar que los espacios generen un error o bugs
    rut = rut.strip().replace(".", "").replace("-", "")
    
    if len(rut) < 2:
        return False
    
    numero_del_rut = rut[:-1]
    digito_verificador = rut[-1].upper()
    
    
    if not numero_del_rut.isdigit():
        return False
    
    suma = 0
    multiplicador = 2
    
    for i in reversed(range(len(numero_del_rut))):
        suma += int(numero_del_rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2 #Ternario
        
    digito_verificador_calculado = 11 - (suma % 11)
    
    if digito_verificador_calculado == 11:
        digito_verificador_calculado = '0'
    
    elif digito_verificador_calculado == 10:
        digito_verificador_calculado = 'K'
        
    return str(digito_verificador_calculado) == digito_verificador


#POST
def crear_proveedor(nombre,rut,telefono,correo,calle,comuna,ciudad,numero):
    
    
    #Validaciones de Info en DB
    if not validar_rut:
        return False
    
    if existe_rut(rut):
        return False
    
    if existe_telefono(telefono):
        return False
    
    if existe_correo(correo):
        return False
    
    
    nuevo_proveedor = Proveedor()
    nuevo_proveedor.nombre = nombre
    nuevo_proveedor.rut = rut
    nuevo_proveedor.telefono = telefono
    nuevo_proveedor.correo = correo
    
    nueva_direccion = crear_direccion(calle,ciudad,comuna,numero)
    
    if not guardar_direcciones(nueva_direccion):
        return False
    
    nuevo_proveedor.id_direccion = nueva_direccion
    return guardar_proveedor(nuevo_proveedor)


#GET_BY_ID
def obtener_proveedor(id_proveedor):
    try:
        return Proveedor[id_proveedor]
    except Proveedor.DoesNotExist:
        return None
    
#UPDATE_FOR ID
def actualizar_proveedor_existente(id_proveedor,nombre,telefono,correo):
    
    proveedor = obtener_proveedor(id_proveedor)
    
    if proveedor == None:
        return False
    
    if existe_correo(correo):
        return False
    
    if existe_telefono(telefono):
        return False
    
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.correo = correo
    
    actualizar_proveedor(proveedor)

#UPDATE_ONLY_DIRECCION
#Idea traida desde la rama de Axwel
def actualizar_direccion_existente(id_proveedor,ciudad,comuna,calle,numero):
    
    proveedor = obtener_proveedor(id_proveedor)
    
    if proveedor == None:
        return False
    
    direccion = proveedor.id_direccion
    return actualizar_direccion(direccion,ciudad,comuna,calle,numero)


#DELETE
def desactivar_proveedor(id_proveedor):
    
    proveedor = obtener_proveedor(id_proveedor)
    
    if proveedor is None:
        return False
    
    proveedor.estado = False
    return borrado_logico_proveedor(proveedor)