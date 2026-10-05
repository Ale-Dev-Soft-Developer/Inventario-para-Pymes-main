from peewee import CharField,AutoField,ForeignKeyField,Model,BooleanField,SQL
from datos.modelos import BaseModel
from auxiliares.mensajes import valor_por_defecto
from datos.modelos.direccion import Direccion as Direcciones



class Almacen(BaseModel):
    encargado = CharField(max_length=50)
    estado = BooleanField(constraints=[SQL(valor_por_defecto)])
    id_almacen = AutoField()
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direcciones)
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'almacenes'