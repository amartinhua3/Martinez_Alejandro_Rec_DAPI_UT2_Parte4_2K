def create_email(nombre, apellido):
    '''Crea un correo electrónico a partir de nombre y apellido, con el dominio "@educacion.navarra.es".
    Parametros:
    - nombre: str con el nombre de la persona
    - apellido: str con el apellido de la persona
    Return:
    - str con el correo electrónico generado
    '''
    if len(apellido) >= 5:
        return str(nombre[0]).lower() + str(apellido[0:5]).lower() + '@educacion.navarra.es'
    else:
        return str(nombre[0]).lower() + str(apellido[0:len(apellido)]).lower() + '@educacion.navarra.es'