import csv
from datetime import datetime


# Función para validar la fecha
def validar_fecha(fecha):
    try:
        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S.%f')
        return fecha_obj.year > 1900
    except ValueError:
        return False


# Ruta al archivo CSV
archivo_csv = './data/tabla1.txt'

with open(archivo_csv, 'r', newline='') as file:
    lector_csv = csv.reader(file, delimiter='\t')

    for linea in lector_csv:
        valida = True

        for campo in linea:
            if not valida:
                break
            try:
                fecha_obj = datetime.strptime(campo, '%Y-%m-%d %H:%M:%S.%f')
                if fecha_obj.year < 1900:
                    valida = False
                    pass
            except ValueError:
                pass

        if not valida:
            print("Línea inválida:", linea)


# with open(archivo_csv, 'r', newline='') as file:
#     lector_csv = csv.reader(file, delimiter='\t')
#
#     for linea in lector_csv:
#         if len(linea) >= 10:
#             fecha1_valida = validar_fecha(linea[9])
#             fecha2_valida = validar_fecha(linea[10])
#
#             if fecha1_valida and fecha2_valida:
#                 print("Línea válida:", linea)
#             else:
#                 print("Línea inválida:", linea)
#         else:
#             print("Línea no tiene suficientes campos:", linea)