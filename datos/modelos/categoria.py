from peewee import CharField,AutoField
from datos.modelos import BaseModel

class Categoria(BaseModel):
    descripcion = CharField()
    id_categoria = AutoField()
    nombre = CharField(max_length=50)
    
    class Meta:
        table_name = 'categorias'