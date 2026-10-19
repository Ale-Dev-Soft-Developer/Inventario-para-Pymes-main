from datos.modelos.direccion import Direccion
from datos.repositorios.repositorio_direccion import guardar_direcciones
from peewee import PeeweeException
from auxiliares.mensajes import excepcion_peewee
from datos.modelos.models import database


def crear_direccion(calle, numero, comuna, ciudad):
    
    if calle == '' or numero == '' or comuna == '' or ciudad == '':
        return False
    
    try: 
        
        with database.atomic():
        
            nueva_direccion = Direccion()
            nueva_direccion.calle = calle
            nueva_direccion.numero = numero
            nueva_direccion.comuna = comuna
            nueva_direccion.ciudad = ciudad
            
            
            return guardar_direcciones(nueva_direccion)
            
        
    except PeeweeException as e:
        print(excepcion_peewee(e))
        


def actualizar_direccion(direccion, calle, numero, comuna, ciudad):
    
    if direccion == '' or calle == '' or numero == '' or comuna == '' or ciudad == '':
            return False

    try: 
        
        with database.atomic():
            
            direccion.calle = calle
            direccion.numero = numero
            direccion.comuna = comuna
            direccion.ciudad = ciudad
            direccion.direccion = direccion    
    
            guardar_direcciones(actualizar_direccion)
        
    except PeeweeException as e:
        print(excepcion_peewee(e))