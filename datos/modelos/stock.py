from peewee import CharField,AutoField,IntegerField,ForeignKeyField,Model
from datos.modelos import BaseModel
from datos.modelos.producto import Producto as Productos


class Stock(BaseModel):
    id_stock = AutoField()
    stock_actual = IntegerField()
    stock_minimo = IntegerField()

    class Meta:
        table_name = 'stock'