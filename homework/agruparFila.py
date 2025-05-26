from homework.filaNueva import filaNueva
from homework.cargaYLimpiezaFilas import cargaYLimpiezaFilas
def agruparFila():
    lineas = cargaYLimpiezaFilas()

    filas = []
    fila_actual = ''

    for linea in lineas:
        if filaNueva(linea):
            if fila_actual:
                filas.append(fila_actual.strip())
            fila_actual = linea
        else:
            fila_actual += ' ' + linea

    if fila_actual:
        filas.append(fila_actual.strip())
    
    return filas