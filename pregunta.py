"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def processing(var):
    line = []
    line.append(int(var[3:8]))
    line.append(int(var[9:15]))
    line.append(float(var[25:29].replace(',', '.')))
    fetch = var[41:]
    fetch = fetch.replace('\n', '')
    fetch = fetch.replace('.', '')
    fetch = re.sub(r' +', ' ', fetch)
    line.append(fetch)
    return line


def ingest_data():

    with open ("clusters_report.txt", "r") as raw:
        data = raw.readlines()

    # Tittle format
    tittle = data[:2]
    tittle = list(map(lambda x : x.replace("\n", ""), tittle))
    tittle = list(map(lambda x : x.strip(), tittle))
    tittle = list((map(lambda x : re.split(r' {2,}',x), tittle)))
    header = tittle[0]
    aux = tittle[1]
    header[1] = header[1] + " " + aux[0]
    header[2] = header[2] + " " + aux[1]

    header = list(map(lambda x : x.lower(), header))
    header = list(map(lambda x : x.replace(' ', '_'),header))

    # Row format
    data = data[4:]

    test = ""
    test = test.join(data)
    test = re.split(r'\n *\n', test)
    test = list(filter(lambda x : x != '', test))
    test = list(map(processing, test))
    df = pd.DataFrame(test, columns=header)

    return(df)

print(ingest_data())