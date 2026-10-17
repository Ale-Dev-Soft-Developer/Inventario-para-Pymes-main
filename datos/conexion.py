from peewee import MySQLDatabase
from decouple import config

def conectar_db():
    base_datos = MySQLDatabase(config('db'),
                               **{
                                   'charset': 'utf8mb4',
                                   'host': config('host'),
                                   'port': config('port', cast=int),
                                   'user': config('user'),
                                    'password': config('password'),
                                    'sql_mode': 'STRICT_TRANS_TABLES'
                                })
    return base_datos