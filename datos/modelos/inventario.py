from peewee import CompositeKey, DateField,CharField,AutoField,IntegerField,BooleanField,SQL,ForeignKeyField,Model,DateTimeField
from decouple import config
from auxiliares.mensajes import valor_por_defecto
from datos.conexion import conectar_db
from datos.modelos import BaseModel
from datos.modelos.direccion import Direccion as Direcciones
from datos.modelos.categoria import Categoria as Categorias
from datos.modelos.almacen import Almacen as Almacenes
from datos.modelos.producto import Producto as Productos
from datos.modelos.stock import Stock as Stocks



class Inventario(BaseModel):
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacenes)
    id_inventario = AutoField()
    id_producto = ForeignKeyField(column_name='id_producto', field='id_producto', model=Productos)
    id_stock = ForeignKeyField(column_name='id_stock', field='id_stock', model=Stocks, unique=True)
    
    class Meta:
        table_name = 'inventarios'
        indexes = (
            (('id_producto','id_almacen'), True),
        )