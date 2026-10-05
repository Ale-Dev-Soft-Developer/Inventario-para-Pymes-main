from peewee import CharField,AutoField,IntegerField,ForeignKeyField,BooleanField,CompositeKey,SQL
from auxiliares.mensajes import valor_por_defecto
from datos.modelos.producto import Producto as Productos
from datos.modelos.proveedor import Proovedor as Proveedores
from datos.modelos import BaseModel

class ProductoProveedor(BaseModel):
    es_principal = BooleanField(constraints=[SQL(valor_por_defecto)])
    id_producto = ForeignKeyField(column_name='id_producto', field='id_producto', model=Productos)
    id_proveedor = ForeignKeyField(column_name='id_proveedor', field='id_proveedor', model=Proveedores)

    class Meta:
        table_name = 'producto_proveedor'
        indexes = (
            (('id_producto', 'id_proveedor'), True),
        )
        primary_key = CompositeKey('id_producto', 'id_proveedor')
