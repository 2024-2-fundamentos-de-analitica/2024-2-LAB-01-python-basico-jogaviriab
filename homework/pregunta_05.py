"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv",mode="r") as file:
        data = file.readlines()
    
    dic = {}
    result = []
    for line in data:
        l = line.split("	")[0]
        v = int(line.split("	")[1])
        if l not in dic:
            dic[l] = [v,v]
        else:
            if v > dic[l][0]:
                dic[l] = [v,dic[l][1]]
            elif v < dic[l][1]:
                dic[l] = [dic[l][0],v]
    for val in dic.items():
        r = (val[0],val[1][0],val[1][1])
        result.append(r)
    result.sort()
    return result

print(pregunta_05())