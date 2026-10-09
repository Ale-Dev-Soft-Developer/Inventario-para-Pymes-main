valor_por_defecto = 'DEFAULT 1'

# Datos de categoria
ingrese_id_categoria = 'Ingrese el ID de la categoria: '
ingrese_nombre_categoria = 'Ingrese el nombre de la categoria: '
ingrese_descripcion_categoria = 'Ingrese la descripcion de la categoria: '


def ingresaras_lo_siguiente(nombre,descripcion):
    return f'Ingresaras la Categoria: {nombre}, con la descripcion: {descripcion}'

# Validaciones
id_debe_ser_entero = 'El ID debe ser un numero entero.'
categoria_por_id_no_existe = 'No existe una categoria con el ID ingresado.'

def no_existe(nombre):
    return f'No se encontraron registros de {nombre}.'


# Eliminar categoria (llevan {nombre} asi que implemento una funcion que lo entregue listo
def confirmar_borrar_categoria(respuesta):
    return f'Estas seguro de borrar la categoria: {respuesta}?  (S/N): '


def categoria_borrada_exito(nombre):
    return f"Categoria '{nombre}' borrada con exito."

categoria_no_borrada = 'No se pudo borrar.'

# Respuestas generales
solo_numeros_enteros = 'Ingresa solo numeros Enteros.'
opcion_cancelada = 'Operacion Cancelada.'
opcion_invalida = 'Operacion invalida.'
programa_finalizado = 'Programa Finalizado'
estas_seguro = '¿Estas seguro? S/N: '
operacion_exitosa = 'Operacion Exitosa'

# Producto
ingrese_id_producto = 'Ingrese el ID del producto: '
ingrese_nombre_producto = 'Ingrese el nombre del producto: '
ingrese_descripcion_producto = 'Ingrese la descripcion del producto: '
ingrese_id_categoria_producto = 'Ingrese el ID de la categoria del producto: '
ingrese_sku = 'Ingrese el SKU del producto: '
ingrese_precio_costo = 'Ingrese el precio de costo del producto: '
ingrese_precio_venta = 'Ingrese el precio de venta del producto: '
ingrese_fecha_vencimiento = 'Ingrese la fecha de vencimiento (AAAA-MM-DD) o Enter si no aplica: '
ingrese_fecha_elaboracion = 'Ingrese la fecha de elaboracion (AAAA-MM-DD) o Enter si no aplica: '
producto_por_id_no_existe = 'No existe un producto con el ID ingresado.'


# Validaciones de entrada
campo_obligatorio = 'Este campo no puede estar vacio.'
fecha_invalida = 'Fecha invalida. Use el formato AAAA-MM-DD.'

def ingresaras_producto(nombre, descripcion):
    return f'Ingresaras el Producto: {nombre}, con la descripcion: {descripcion}'


def titulo_actualizar_producto(id_producto):
    return f'\n--- Actualizando producto ID {id_producto} ---'


def pregunta_modificar(campo, valor_actual):
    return f'¿Deseas modificar {campo} ({valor_actual})? (s/n): '

def confirmar_borrar_producto(respuesta):
    return f'Estas seguro de borrar el producto: {respuesta}?  (S/N): '