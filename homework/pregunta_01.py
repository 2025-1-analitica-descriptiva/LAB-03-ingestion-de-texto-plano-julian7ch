"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def filaNueva(linea):
    return re.match(r'^\d+', linea) is not None

def pregunta_01():
    with open('./files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = lines[4:]
        lines = [line.strip() for line in lines if line.strip() != '']

        filas = []
        fila_actual = ''

        for linea in lines:
            if filaNueva(linea):
                if fila_actual:
                    filas.append(fila_actual.strip())
                fila_actual = linea
            else:
                fila_actual += ' ' + linea

        if fila_actual:
            filas.append(fila_actual.strip())

        data = []

        for fila in filas:
            match = re.match(r'^(\d+)\s+(\d+)\s+([\d,]+ %)\s+(.*)', fila)
            if match:
                cluster = int(match.group(1))
                cantidad = int(match.group(2))
                porcentaje = float(match.group(3).replace(',', '.').replace('%', '').strip())
                palabras_clave = match.group(4)

                palabras_clave = re.sub(r'\s+', ' ', palabras_clave)
                palabras_clave = palabras_clave.replace(' ,', ',').strip()
                if palabras_clave.endswith('.'):                           
                  palabras_clave = palabras_clave[:-1]

                data.append([cluster, cantidad, porcentaje, palabras_clave])

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