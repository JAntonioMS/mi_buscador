class ResultadosClass:
    def __init__(self, url, apariciones):
        self.url = url
        self.apariciones = apariciones

def buscar_palabra(busqueda):
    archivo_indice = 'C:/Users/juanm/Programacion/DJANGO/buscador/buscador/resultado.txt'

    with open(archivo_indice, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        if busqueda + ':' in linea:
            informacion = linea.replace(busqueda + ': ', '').strip()
            informacion = eval(informacion)
            return informacion

    return f'La palabra "{busqueda}" no se encuentra en el índice invertido.'

def convertir_cadena_a_objetos(cadena):
    cadena_de_texto = str(cadena)
    lista_tuplas = eval(cadena_de_texto)
    lista_objetos = [ResultadosClass(url, apariciones) for url, apariciones in lista_tuplas]
    return lista_objetos