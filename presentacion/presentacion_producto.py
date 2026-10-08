from negocio.negocio_producto import crear_producto, obtener_producto, actualizar_producto_existente
from auxiliares.entradas import (
    pedir_texto,
    pedir_entero,
    pedir_fecha_opcional,
    pedir_confirmacion,
    desea_modificar,
)
from auxiliares.mensajes import (
    ingrese_id_producto,
    ingrese_nombre_producto,
    ingrese_descripcion_producto,
    ingrese_id_categoria_producto,
    ingrese_sku,
    ingrese_precio_costo,
    ingrese_precio_venta,
    ingrese_fecha_vencimiento,
    ingrese_fecha_elaboracion,
    producto_por_id_no_existe,
    id_debe_ser_entero,
    ingresaras_producto,
    titulo_actualizar_producto,
    estas_seguro,
    opcion_cancelada,
)


def solicitar_datos_producto():
    nombre = pedir_texto(ingrese_nombre_producto)
    descripcion = pedir_texto(ingrese_descripcion_producto)
    categoria = pedir_entero(ingrese_id_categoria_producto)
    sku = pedir_texto(ingrese_sku)
    precio_costo = pedir_entero(ingrese_precio_costo)
    precio_venta = pedir_entero(ingrese_precio_venta)
    fecha_vencimiento = pedir_fecha_opcional(ingrese_fecha_vencimiento)
    fecha_elaboracion = pedir_fecha_opcional(ingrese_fecha_elaboracion)

    print(ingresaras_producto(nombre, descripcion))

    if not pedir_confirmacion(estas_seguro):
        print(opcion_cancelada)
        return None

    return crear_producto(
        nombre = nombre,
        descripcion = descripcion,
        categoria = categoria,
        sku = sku,
        precio_costo = precio_costo,
        precio_venta = precio_venta,
        fecha_vencimiento = fecha_vencimiento,
        fecha_elaboracion = fecha_elaboracion,
    )


def actualizar_datos_producto():
    try:
        id_producto = int(input(ingrese_id_producto))
    except ValueError:
        print(id_debe_ser_entero)
        return

    # Si existe, obtenemos el objeto Producto y si no existe obtenemos None
    producto = obtener_producto(id_producto)

    if producto is None:
        print(producto_por_id_no_existe)
        return

    print(titulo_actualizar_producto(id_producto))

    #Se pregunta campo por camnpo si desea actualizar.
    nombre = producto.nombre
    if desea_modificar("el nombre", nombre):
        nombre = pedir_texto(ingrese_nombre_producto)

    descripcion = producto.descripcion
    if desea_modificar("la descripcion", descripcion):
        descripcion = pedir_texto(ingrese_descripcion_producto)

    categoria = producto.id_categoria
    if desea_modificar("la categoria", categoria):
        categoria = pedir_entero(ingrese_id_categoria_producto)

    sku = producto.sku
    if desea_modificar("el SKU", sku):
        sku = pedir_texto(ingrese_sku)

    precio_costo = producto.precio_costo
    if desea_modificar("el precio de costo", precio_costo):
        precio_costo = pedir_entero(ingrese_precio_costo)

    precio_venta = producto.precio_venta
    if desea_modificar("el precio de venta", precio_venta):
        precio_venta = pedir_entero(ingrese_precio_venta)

    fecha_vencimiento = producto.fecha_vencimiento
    if desea_modificar("la fecha de vencimiento", fecha_vencimiento):
        fecha_vencimiento = pedir_fecha_opcional(ingrese_fecha_vencimiento)

    fecha_elaboracion = producto.fecha_elaboracion
    if desea_modificar("la fecha de elaboracion", fecha_elaboracion):
        fecha_elaboracion = pedir_fecha_opcional(ingrese_fecha_elaboracion)

    # retorna a la Capa de Negocio
    return actualizar_producto_existente(
        id_producto, nombre, descripcion, categoria, sku,
        precio_costo, precio_venta, fecha_vencimiento, fecha_elaboracion
    )