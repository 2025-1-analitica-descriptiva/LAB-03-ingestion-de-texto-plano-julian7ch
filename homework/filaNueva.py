import re
def filaNueva(linea):
    return re.match(r'^\d+', linea) is not None