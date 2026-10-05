from peewee import CharField,AutoField,BooleanField,ForeignKeyField,SQL
from auxiliares.mensajes import valor_por_defecto
from datos.modelos.direccion import Direccion as Direcciones
from datos.modelos import BaseModel

class Proovedor (BaseModel):
    correo = CharField(max_length=100, null=True,unique=True)
    estado = BooleanField(constraints=[SQL(valor_por_defecto)])
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direcciones)
    id_proveedor = AutoField()
    nombre = CharField(max_length=50)
    rut = CharField(max_length=12, unique=True)
    telefono = CharField(max_length=9, unique=True)
    
    class Meta:
        table_name = 'proveedores'