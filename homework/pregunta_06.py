"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as file:
        data = file.readlines()
    print(max(3,3))
    dic = {}
    result = []
    for line in data:
        info = line.split("	")[4]
        info = info.replace("\n","").split(",")
        for i in info:
            clave,valor = i.split(":")
            valor = int(valor)
            if clave in dic:
                dic[clave][0]=min(dic[clave][0],valor)
                dic[clave][1]=max(dic[clave][1],valor)
            else:
                dic[clave] = [valor,valor]   
    
    [result.append((item[0],int(item[1][0]),int(item[1][1]))) for item in dic.items()]
    result.sort()
    return result

print(pregunta_06())