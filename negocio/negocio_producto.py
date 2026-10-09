from datos.repositorios.repositorio_producto import listado_productos as obtener_listado_productos,guardar_producto,actualizar_producto,borrado_logico_producto
from datos.modelos.producto import Producto
from prettytable import PrettyTable
from auxiliares.mensajes import no_existe

#GET
def listado_productos():
    
    tabla_producto = PrettyTable()
    tabla_producto.field_names = ["ID", "Nombre", "Descripción", "Categoria", "SKU", "Precio Costo", "Precio Venta", "Fecha Vencimiento", "Fecha Elaboracion", "Estado"]
    
    data_de_productos = obtener_listado_productos() #instancia para revisar la data de la tabla
    
    if data_de_productos:
        
        for producto in data_de_productos:
            tabla_producto.add_row([
                producto.id_producto,
                producto.nombre,
                producto.descripcion,
                producto.id_categoria,
                producto.sku,
                producto.precio_costo,
                producto.precio_venta,
                producto.fecha_vencimiento,
                producto.fecha_elaboracion,
                producto.estado])
        print(tabla_producto)
    
    if not data_de_productos:
        print(no_existe(data_de_productos))
        

#POST
def crear_producto(nombre,descripcion,categoria,sku,precio_costo,precio_venta,fecha_vencimiento,fecha_elaboracion):
    nuevo_producto = Producto()
    nuevo_producto.nombre = nombre
    nuevo_producto.descripcion = descripcion
    nuevo_producto.id_categoria = categoria
    nuevo_producto.sku = sku
    nuevo_producto.precio_costo = precio_costo
    nuevo_producto.precio_venta = precio_venta
    nuevo_producto.fecha_vencimiento = fecha_vencimiento
    nuevo_producto.fecha_elaboracion = fecha_elaboracion
    return guardar_producto(nuevo_producto)
    

#GET_BY_ID
def obtener_producto(id_producto):
    
    try: 
        return Producto[id_producto]
    except Producto.DoesNotExist:
        return None

#UPDATE_FOR_ID
def actualizar_producto_existente(id_producto,nombre,descripcion,categoria,sku,precio_costo,precio_venta,fecha_vencimiento,fecha_elaboracion):
      
    producto = obtener_producto(id_producto)
      
    if producto == None:
          return False
    
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.id_categoria = categoria
    producto.sku = sku
    producto.precio_costo = precio_costo
    producto.precio_venta = precio_venta
    producto.fecha_vencimiento = fecha_vencimiento
    producto.fecha_elaboracion = fecha_elaboracion
    
    actualizar_producto(producto)
    

#DELETE
# Metodo para (borrado logico)
def desactivar_producto(id_producto):
    producto = obtener_producto(id_producto)

    if producto is None:
        return False

    # estado es un booleano, solo necesito cambiarlo a False para desactivarlo
    producto.estado = False
    return borrado_logico_producto(producto)