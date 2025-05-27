import re

from homework.procesarRegistro import procesarRegistro

def extraerDatosDesdeFilas(filas):
    data = []
    registroActual = ""

    for fila in filas:
        if re.match(r'^\d+\s+\d+\s+[\d,]+ %', fila):
            if registroActual:
                dato = procesarRegistro(registroActual)
                if dato:
                    data.append(dato)
            registroActual = fila  
        else:
            registroActual += " " + fila.strip()

    if registroActual:
        dato = procesarRegistro(registroActual)
        if dato:
            data.append(dato)

    return data


