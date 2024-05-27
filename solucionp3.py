def calculate_grade(practica01, practica02, practica03, examen, recuperacion, actitud):
    '''Esta funcion calcula la nota media de un alumno
    Parametros:
        - Práctica 01: float
        - Práctica 02: float
        - Práctica 03: float
        - Examen: float
        - Recuperación: float
        - Actitud: float
    Return:
        - Nota final: float con la nota final del alumno
        - Aprobado: booleano. Si ha aprobado true, si ha suspendido false'''
   
    nota_final = ((practica01 + practica02 + practica03) / 3 * 0.3
    + max(examen,recuperacion) * 0.6 + actitud * 0.1)


    if nota_final >= 5:
        aprobado =  True
    else:
        aprobado = False
    return nota_final, aprobado
