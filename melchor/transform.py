import csv
from datetime import datetime

archivo_csv = './data/tabla1.txt'
archivo_salida = './data/tabla1_modificado.txt'

with open(archivo_csv, 'r', newline='') as file:
    lector_csv = csv.reader(file, delimiter='\t')
    lineas_modificadas = []

    for linea in lector_csv:
        linea_modificada = []
        valida = True

        for campo in linea:
            try:
                fecha_obj = datetime.strptime(campo, '%Y-%m-%d %H:%M:%S.%f')
                if fecha_obj.year < 1900:
                    valida = False
                    linea_modificada.append("1900-00-00 00:00:00.000")
                else:
                    linea_modificada.append(campo)
            except ValueError:
                valida = False
                linea_modificada.append(campo)

        if valida:
            lineas_modificadas.append(linea_modificada)
        else:
            lineas_modificadas.append(linea_modificada)
            print("Línea inválida:", linea)

# Guardar el archivo modificado
with open(archivo_salida, 'w', newline='') as file_salida:
    escritor_csv = csv.writer(file_salida, delimiter='\t')
    escritor_csv.writerows(lineas_modificadas)

print(f"Archivo modificado guardado en {archivo_salida}")