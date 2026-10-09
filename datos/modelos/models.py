from peewee import Model
from datos.conexion import conectar_db

#Conexion con mi DB
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database