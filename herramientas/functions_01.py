from data_stark import lista_personajes
from .functions_00 import *

def filtar_por_generos(lista:list, gen:str):
    """
    Filtra una lista de personajes por género.

    Args:
        lista (list): Lista de personajes.
        gen (str): Género por el cual se desea filtrar (e.g., 'M' o 'F').

    Returns:
        list: Lista de personajes que corresponden al género especificado.
    """
    validar_lista(lista)
    
    lista_return = []
    for el in lista:
        if el["genero"] == gen:
            lista_return.append(el)
    return lista_return

def mostrar_por_generos(lista:list, gen:str):
    """
    Muestra por consola los personajes filtrados por género.

    Args:
        lista (list): Lista de personajes.
        gen (str): Género por el cual se desea filtrar (e.g., 'M' o 'F').
    """
    heroe = filtar_por_generos(lista, gen)
    
    for el in heroe:
        print(f"Nombre: {el["nombre"]}, Genero: {el["genero"]}")

def maxmin_genero(lista:list, gen:str, campo:str, minmax:str):
    """
    Obtiene el personaje con el valor máximo o mínimo de un campo específico dentro de un género.

    Args:
        lista (list): Lista de personajes.
        gen (str): Género por el cual se desea filtrar (e.g., 'M' o 'F').
        campo (str): Campo a evaluar (e.g., 'altura').
        minmax (str): Especifica si se desea obtener el valor máximo o mínimo ('max' o 'min').

    Returns:
        dict: El personaje con el valor máximo o mínimo del campo especificado.
    """
    
    lista_gen = filtar_por_generos(lista, gen)
    resultado =obtener_minmax(lista_gen, minmax, campo)
    return resultado

def mostrar_maxmin_genero(lista:list, gen:str, campo:str, minmax:str):
    """
    Muestra por consola el personaje con el valor máximo o mínimo de un campo específico dentro de un género.

    Args:
        lista (list): Lista de personajes.
        gen (str): Género por el cual se desea filtrar (e.g., 'M' o 'F').
        campo (str): Campo a evaluar (e.g., 'altura').
        minmax (str): Especifica si se desea obtener el valor máximo o mínimo ('max' o 'min').
    """
    heroe = maxmin_genero(lista, gen, campo, minmax)
    match minmax:
        case "max":
            msj = f"El superhéroe {gen} con mayor {campo} es {heroe[0]}, midiendo {heroe[1]}cm"
        case "min":
            msj = f"El superhéroe {gen} con menor {campo} es {heroe[0]}, midiendo {heroe[1]}cm"
    print(msj)

def obtener_promedio_altura_gen(lista:list, gen:str):
    """
    Calcula el promedio de altura de los personajes de un género específico.

    Args:
        lista (list): Lista de personajes.
        gen (str): Género por el cual se desea filtrar (e.g., 'M' o 'F').

    Returns:
        float: Promedio de altura de los personajes del género especificado.
    """
    lista_genero = filtar_por_generos(lista, gen)
    suma_alturas = 0
    
    for elm in lista_genero:
        suma_alturas = suma_alturas + float(elm["altura"])
    return suma_alturas / len(lista_genero)

def case_h():
    """
    Ejecuta y muestra resultados de análisis de alturas para personajes masculinos y femeninos,
    incluyendo los máximos, mínimos y promedios.
    """
    mostrar_maxmin_genero(lista_personajes, "M", "altura", "max")
    mostrar_maxmin_genero(lista_personajes, "M", "altura", "min")
    print("")
    mostrar_maxmin_genero(lista_personajes, "F", "altura", "max")
    mostrar_maxmin_genero(lista_personajes, "F", "altura", "min")
    print("")
    promedio_m = obtener_promedio_altura_gen(lista_personajes, "M")
    promedio_f = obtener_promedio_altura_gen(lista_personajes, "F")
    print(f"Promedio de altura superhéroes M: {promedio_m:.2f}")
    print(f"Promedio de altura superhéroes F: {promedio_f:.2f}")

def filtar_por_campo(lista:list, campo:str, parametro:str):
    """
    Filtra y muestra por consola los personajes según un campo y su valor específico.

    Args:
        lista (list): Lista de personajes.
        campo (str): Campo por el cual se desea filtrar (e.g., 'color_ojos').
        parametro (str): Valor del campo para filtrar los personajes.

    Returns:
        list: Lista de personajes que corresponden al valor del campo especificado.
    """
    lista_return = []
    for el in lista:
        if el[f"{campo}"] == parametro:
            lista_return.append(el)
    
    for el in lista_return:
        print(f"Nombre: {el["nombre"]} | {campo.capitalize()}: {el[f"{campo}"]}")

def case_i():
    """
    Muestra por consola los personajes filtrados por diversos colores de ojos.
    """
    print("COLORES DE OJOS:")
    print("Brown: ")
    filtar_por_campo(lista_personajes, "color_ojos", "Brown")
    print("")
    print("Yellow (without irises): ")
    filtar_por_campo(lista_personajes, "color_ojos", "Yellow (without irises)")
    print("")
    print("Hazel: ")
    filtar_por_campo(lista_personajes, "color_ojos", "Hazel")
    print("")
    print("Blue: ")
    filtar_por_campo(lista_personajes, "color_ojos", "Blue")
    print("")
    print("Green: ")
    filtar_por_campo(lista_personajes, "color_ojos", "Green")
    print("")
    print("Red: ")
    filtar_por_campo(lista_personajes, "color_ojos", "Red")

def case_j():
    """
    Muestra por consola los personajes filtrados por diversos colores de pelo.
    """
    print("COLORES DE PELO:")
    print("Yellow:")
    filtar_por_campo(lista_personajes, "color_pelo", "Yellow")
    print("")
    print("Brown:")
    filtar_por_campo(lista_personajes, "color_pelo", "Brown")
    print("")
    print("Black:")
    filtar_por_campo(lista_personajes, "color_pelo", "Black")
    print("")
    print("Auburn:")
    filtar_por_campo(lista_personajes, "color_pelo", "Auburn")
    print("")
    print("Red / Orange:")
    filtar_por_campo(lista_personajes, "color_pelo", "Red / Orange")
    print("")
    print("White:")
    filtar_por_campo(lista_personajes, "color_pelo", "White")
    print("")
    print("No Hair:")
    filtar_por_campo(lista_personajes, "color_pelo", "No Hair")
    print("")
    print("Blond:")
    filtar_por_campo(lista_personajes, "color_pelo", "Blond")
    print("")
    print("Sin color de pelo:")
    filtar_por_campo(lista_personajes, "color_pelo", "")

def case_k():
    """
    Muestra por consola los personajes filtrados por diversos niveles de inteligencia.
    """
    print("NIVELES DE INTELIGENCIA:")
    print("Sin nivel de inteligencia:")
    filtar_por_campo(lista_personajes, "inteligencia", "")
    print("")
    print("Inteligencia promedio:")
    filtar_por_campo(lista_personajes, "inteligencia", "average")
    print("")
    print("Inteligencia buena:")
    filtar_por_campo(lista_personajes, "inteligencia", "good")
    print("")
    print("Inteligencia alta:")
    filtar_por_campo(lista_personajes, "inteligencia", "high")