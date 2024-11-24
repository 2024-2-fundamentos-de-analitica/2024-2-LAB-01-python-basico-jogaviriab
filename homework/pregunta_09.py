"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as file:
        data = file.readlines()
    result = {}
    for line in data:
        info = line.split("	")[4]
        info = info.replace("\n","").split(",")
        for i in info:
            clave,_ = i.split(":")
            result[clave] = result[clave] + 1 if clave in result else 1

    
    return result