from peewee import CharField,AutoField,BooleanField,SQL,ForeignKeyField,Model,IntegerField,DateField
from auxiliares.mensajes import valor_por_defecto
from datos.modelos.models import BaseModel
from datos.modelos.categoria import Categoria as Categorias


class Producto(BaseModel):
    descripcion = CharField()
    estado = BooleanField(constraints=[SQL(valor_por_defecto)])
    fecha_elaboracion = DateField(null=True)
    fecha_vencimiento = DateField(null=True)
    id_categoria = ForeignKeyField(column_name='id_categoria', field='id_categoria', model=Categorias)
    id_producto = AutoField()
    nombre = CharField(max_length=50)
    precio_costo = IntegerField()
    precio_venta = IntegerField()
    sku = CharField(max_length=100, unique=True)

    class Meta:
        table_name = 'productos'
