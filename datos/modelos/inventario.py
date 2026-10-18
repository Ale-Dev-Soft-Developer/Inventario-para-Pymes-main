from peewee import AutoField,SQL,ForeignKeyField,IntegerField
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
    id_inventario = AutoField()
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacenes)
    id_producto = ForeignKeyField(column_name='id_producto', field='id_producto', model=Productos)
    stock_actual = IntegerField()
    stock_minimo = IntegerField()
    
    class Meta:
        table_name = 'inventarios'
        indexes = (
            (('id_producto','id_almacen'), True),
        )