"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

from homework.cargaYLimpiezaFilas import cargaYLimpiezaFilas
from homework.extraerDatosDesdeFilas import extraerDatosDesdeFilas

def pregunta_01():
    lineas = cargaYLimpiezaFilas()
    # print(lineas)
    data = extraerDatosDesdeFilas(lineas)
    # print(data)
    dataFrame = pd.DataFrame(data, columns=[
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ])

    # pd.set_option('display.max_colwidth', None)  # None = sin límite de caracteres por celda
    # pd.set_option('display.max_columns', None)   # Muestra todas las columnas
    # pd.set_option('display.width', 0)            # Autoajusta el ancho
    # print(dataFrame['principales_palabras_clave'].to_list())

    print(dataFrame)
    return dataFrame

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
pregunta_01()