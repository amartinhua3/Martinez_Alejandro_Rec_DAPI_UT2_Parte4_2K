from solucionp2 import create_email 
from solucionp3 import calculate_grade 
import csv
def process_class(ruta):
    '''Esta función reescribe la lista de alumnos añadiendo los correos electrónicos y las notas finales de cada alumno.
        - Como parametro de entrada hay una string que es la ruta de acceso al archivo csv
        - Como parámetro de salida no hay '''
    alumnado = []
    
    with open(ruta, newline='', encoding="UTF-8") as csvfile:
       reader = csv.DictReader(csvfile) 
       
       for fila in reader:
            correo = create_email(fila['Nombre'], fila['Apellido'])
            nota_final, aprobado = calculate_grade(float(fila['Practica01'].replace(',','.')), float(fila['Practica02'].replace(',','.')), 
                            float(fila['Practica03'].replace(',','.')), float(fila['Examen'].replace(',','.')), 
                            float(fila['Recuperacion'].replace(',','.')), float(fila['Actitud'].replace(',','.')))
            fila = {'Nombre' : fila['Nombre'],
                    'Apellido' : fila['Apellido'],
                    'Email' : correo,
                    'Nota Final' : nota_final,
                    'Aprobado' : aprobado}
            alumnado.append(fila)

    with open('grades.csv', 'w', newline='', encoding="UTF-8") as csvfile:
        fieldnames = ['Nombre', 'Apellido', 'Email', 'Nota Final', 'Aprobado'] 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for linea in alumnado:
            writer.writerow(linea)

    return
process_class('class.csv')