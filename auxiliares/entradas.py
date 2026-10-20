from datetime import datetime

from auxiliares.mensajes import (
    opcion_invalida,
    MENSAJE_ID_ENTERO,
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


def forzar_entero(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError:
            print(MENSAJE_ID_ENTERO)
    return numero


def pedir_fecha_opcional(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            return None
        try:
            return datetime.fromisoformat(texto)
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


def forzar_positivo(mensaje):
    valido = False
    while not valido:
        numero = forzar_entero(mensaje)
        if numero > 0:
            valido = True
        else:
            print("Debes ingresar un valor mayor que cero")
    return numero


def campo_obligatorio(mensaje):
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo es obligatorio!")
            continue
        valido = True
    return texto 


def campo_opcional(mensaje, valor_actual):
    valor_nuevo = input(f"{mensaje} (ENTER para mantener): ").strip()

    if valor_nuevo == "":
        return valor_actual
    return valor_nuevo


def forzar_fecha(mensaje, obligatorio=False):
    fecha_valida = False
    while not fecha_valida:
        texto = input(mensaje).strip()
        if texto == "":
            if obligatorio:
                print("La fecha es obligatoria.")
                continue
            return None
        try: 
            fecha = datetime.strptime(texto, "%d-%m-%Y").date()
            fecha_valida = True
        except ValueError:
            print("Ingrese una fecha válida con el formato DD-MM-YYYY.")   
    return fecha 