import re
def extraerDatosDesdeFilas(filas):
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
    
    return data