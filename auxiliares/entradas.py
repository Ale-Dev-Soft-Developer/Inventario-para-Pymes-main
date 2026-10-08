from datetime import date
from auxiliares.mensajes import (
    opcion_invalida,
    solo_numeros_enteros,
    campo_obligatorio,
    fecha_invalida,
    pregunta_modificar,
)


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print(campo_obligatorio)


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print(solo_numeros_enteros)


def pedir_fecha_opcional(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            return None
        try:
            return date.fromisoformat(texto)
        except ValueError:
            print(fecha_invalida)


def pedir_confirmacion(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == 's':
            return True
        if respuesta == 'n':
            return False
        print(opcion_invalida)


def desea_modificar(campo, valor_actual):
    return pedir_confirmacion(pregunta_modificar(campo, valor_actual))