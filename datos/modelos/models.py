from peewee import CompositeKey, DateField,CharField,AutoField,IntegerField,BooleanField,SQL,ForeignKeyField,Model,DateTimeField
from decouple import config
from auxiliares.mensajes import valor_por_defecto
from datos.conexion import conectar_db
from datos.modelos.direccion import Direccion as Direcciones
from datos.modelos.categoria import Categoria as Categorias
from datos.modelos.almacen import Almacen as Almacenes
from datos.modelos.producto import Producto as Productos
from datos.modelos.stock import Stock as Stocks
from datos.modelos.inventario import Inventario as Inventarios
from datos.modelos.proveedor import Proovedor as Proveedores
from datos.modelos.productoProveedor import ProductoProveedor as ProductosProveedores

#Conexion con mi DB
database = conectar_db()


class BaseModel(Model):
    class Meta:
        database = database

    class Meta:
        table_name = 'proveedores'



