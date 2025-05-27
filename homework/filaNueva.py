import re

def filaNueva(linea):
    # Detecta si la línea empieza con uno o más dígitos seguidos de espacios (ej: "1     105")
    return bool(re.match(r'^\d+\s+', linea))
