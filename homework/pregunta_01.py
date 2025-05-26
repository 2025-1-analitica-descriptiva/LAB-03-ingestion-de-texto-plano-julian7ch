"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

from homework.cargaYLimpiezaFilas import cargaYLimpiezaFilas
from homework.extraerDatosDesdeFilas import extraerDatosDesdeFilas

def pregunta_01():
    lineas = cargaYLimpiezaFilas()

    data = extraerDatosDesdeFilas(lineas)

    dataFrame = pd.DataFrame(data, columns=[
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ])
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