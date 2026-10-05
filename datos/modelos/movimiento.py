from peewee import CharField,AutoField,IntegerField,ForeignKeyField,DateTimeField,SQL
from datos.modelos import BaseModel
from datos.modelos.inventario import Inventario as Inventarios


class Movimiento(BaseModel):
    cantidad = IntegerField()
    descripcion = CharField(null=True)
    fecha = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)
    id_inventario = ForeignKeyField(column_name='id_inventario', field='id_inventario', model=Inventarios)
    id_movimiento = AutoField()
    tipo = CharField()
    
    class Meta:
            table_name = 'movimientos'