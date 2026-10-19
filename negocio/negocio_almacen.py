
from datos.repositorios.repositorio_almacen import (listado_almacen as obtener_listado_almacen,
                                                    guardar_almacen,
                                                    obtener_almacen_por_id
                                                    )
from datos.modelos.almacen import Almacen
from negocio.negocio_direccion import (crear_direccion,guardar_direcciones,actualizar_direccion)
from prettytable import PrettyTable

#METODO GET
def listado_almacen():
    
    tabla_almacen = PrettyTable()
    tabla_almacen.field_names = ["ID", "Nombre", "ID_Direccion", "Encargado","Estado"]
    
    data_de_almacen = obtener_listado_almacen()
    
    if data_de_almacen:
        for almacen in data_de_almacen:
            tabla_almacen.add_row([
                almacen.id_almacen,
                almacen.nombre,
                almacen.id_direccion,
                almacen.estado,
                almacen.encargado
            ])
            print(data_de_almacen)
            
    if not almacen:
        return False
    
    

#POST
def crear_almacen(nombre,encargado,calle,ciudad,comuna,numero):

    nuevo_almacen = Almacen()
    nuevo_almacen.nombre = nombre
    nuevo_almacen.encargado = encargado
    
    nueva_direccion = crear_direccion(calle,ciudad,comuna,numero)
    
    if not guardar_direcciones(nueva_direccion):
        return False
    
    nueva_direccion.id_direccion = nueva_direccion
    return guardar_almacen(nuevo_almacen)


#GET_BY_ID
def obtener_almacen(id_almacen):
    
    try:
        return Almacen[id_almacen]
    except Almacen.DoesNotExist:
        return None
    

#UPDATE_ALMACEN
def actualizar_almacen(id_almacen, nombre, encagado):
    almacen = obtener_almacen_por_id(id_almacen)

    if almacen is None:
        return False

    almacen.nombre = nombre
    almacen.encargado = encagado
    return guardar_almacen(almacen)


    
#UPDATE_DIRECCION
def actualizar_direccion_almacen(id_almacen, calle, numero, comuna, ciudad):
    
    almacen = obtener_almacen_por_id(id_almacen)

    if almacen is None:
        return False

    # La relacion (clave foranea) hace que almacen.id_direccion entregue el objeto Direccion
    direccion = almacen.id_direccion
    return actualizar_direccion(direccion, calle, numero, comuna, ciudad)


#DELETE
def borrado_logico_almacen(id_almacen):
    
    almacen = obtener_almacen_por_id(id_almacen)

    if almacen is None:
        return False

    almacen.estado = False
    return guardar_almacen(almacen)