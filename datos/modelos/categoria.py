from peewee import CharField,AutoField,BooleanField
from datos.modelos import BaseModel


class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=50)
    descripcion = CharField()
    estado = BooleanField(default=True)
    
    class Meta:
        table_name = 'categorias'
