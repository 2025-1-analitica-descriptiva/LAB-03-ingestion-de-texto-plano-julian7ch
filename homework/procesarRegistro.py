import re
def procesarRegistro(registro):
    match = re.match(r'^(\d+)\s+(\d+)\s+([\d,]+ %)\s+(.*)', registro)
    if match:
        cluster = int(match.group(1))
        cantidad = int(match.group(2))
        porcentaje = float(match.group(3).replace(',', '.').replace('%', '').strip())
        palabras_clave = match.group(4)

        palabras_clave = re.sub(r'\s+', ' ', palabras_clave)
        palabras_clave = palabras_clave.replace(' ,', ',').strip()
        if palabras_clave.endswith('.'):
            palabras_clave = palabras_clave[:-1]

        return [cluster, cantidad, porcentaje, palabras_clave]
    else:
        return None