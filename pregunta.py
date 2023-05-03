"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import csv
import re

def read_csv():
    matcher = re.compile(r"([0-9]+)\s+([0-9]+)\s+([0-9]+,[0-9]+ %)\s+([\w\s,\-\(\)]+\n+)")
    with open("clusters_report.txt", "r") as raw:
        table = raw.read()
        data = matcher.findall(table)
    for row in data:
        print(row)
    return data


def ingest_data():

    df = read_csv()

    return df

print(ingest_data())