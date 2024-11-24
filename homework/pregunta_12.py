"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open('files/input/data.csv', 'r') as file:
        data = file.readlines()

    result = {}

    for line in data:
        columns = line.split("	")
        letter = columns[0]
        numbers = columns[4].replace("\n","").split(",")
        suma =0
        for number in numbers:
            suma += int(number.split(":")[1])
        result[letter] = result[letter] + suma if letter in result else suma
    
    result = dict(sorted(result.items()))
    return result

