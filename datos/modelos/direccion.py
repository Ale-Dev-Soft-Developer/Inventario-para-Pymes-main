from peewee import CharField,AutoField
from datos.modelos import BaseModel

class Direccion(BaseModel):
    calle = CharField(max_length=50)
    ciudad = CharField(max_length=100)
    comuna = CharField(max_length=100)
    id_direccion = AutoField()
    numero = CharField(max_length=10, null=True)
    
    class Meta:
        table_name = 'direcciones'