import csv

def process_class(ruta):
   """
   Lee los datos y los almacena en una lista de diccionarios donde en cada uno
   de los alumnos las claves serán los datos de la cabecera del archivo CSV
   y los valores serán los datos de cada alumno/a.
   :param ruta: un str con la ruta del fichero (.csv) a abrir.
   :return: None
   """
   alumnado = []
   with open(ruta, newline='', encoding="UTF-8") as csvfile:
       reader = csv.DictReader(csvfile)
       for fila in reader:
           alumnado.append(fila)
   return

process_class("class.csv")