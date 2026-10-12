from datos.repositorios.repositorio_proveedor import listado_proveedor as obtener_listado_proveedor,actualizar_proveedor,guardar_proveedor
from datos.modelos.proveedor import Proovedor
from prettytable import PrettyTable
from auxiliares.mensajes import no_existe

#GET
def obtener_proveedor():
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
