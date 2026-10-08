valor_por_defecto = 'DEFAULT 1'

# Datos de categoria
ingrese_id_categoria = 'Ingrese el ID de la categoria: '
ingrese_nombre_categoria = 'Ingrese el nombre de la categoria: '
ingrese_descripcion_categoria = 'Ingrese la descripcion de la categoria: '

# Validaciones
id_debe_ser_entero = 'El ID debe ser un numero entero.'
categoria_por_id_no_existe = 'No existe una categoria con el ID ingresado.'

def no_existe(nombre):
    return f'No hay {nombre} registrada.'


# Eliminar categoria (llevan {nombre} asi que implem,ento una funcion que lo entregue listo
def confirmar_borrar_categoria(respuesta):
    return f'Estas seguro de borrar la categoria: {respuesta}? (S/N): '

def categoria_borrada_exito(nombre):
    return f"Categoria '{nombre}' borrada con exito."


#def no_se_pudo_borrar(nombre):
    #return f'No se pudo borrar {nombre}'

categoria_no_borrada = 'No se pudo borrar la categoria.'

# Respuestas generales
opcion_cancelada = 'Opcion Cancelada.'
opcion_invalida = 'Opcion invalida.'