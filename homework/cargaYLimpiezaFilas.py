def cargaYLimpiezaFilas():
   with open('./files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = lines[4:]
        lines = [line.strip() for line in lines if line.strip() != '']

        return lines