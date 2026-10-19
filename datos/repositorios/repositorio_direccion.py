from datos.modelos.direccion import Direccion
from peewee import (IntegrityError,
                    OperationalError,
                    DataError,
                    PeeweeException)

from auxiliares.mensajes import (excepcion_peewee,
                                 excepcion_data_error,
                                 excepcion_operational_error,
                                 excepcion_intregity)

def guardar_direcciones(direccion: Direccion):
    
    try:
        
        direccion.save()
        return True
    
    except IntegrityError as e:
        print(excepcion_intregity(e))
    except OperationalError as e:
        print(excepcion_operational_error(e))
    except DataError as e:
        print(excepcion_data_error(e))
    except PeeweeException as e:
        print(excepcion_peewee(e))
        
    return False
        