from homework.filaNueva import filaNueva
from homework.cargaYLimpiezaFilas import cargaYLimpiezaFilas
def agruparFila():
    lineas = cargaYLimpiezaFilas()

    filas = []
    filaActual = ''

    for linea in lineas:
        if filaNueva(linea):
            if filaActual:
                filas.append(filaActual.strip())
            filaActual = linea
        else:
            filaActual += ' ' + linea

    if filaActual:
        filas.append(filaActual.strip())
    
    return filas