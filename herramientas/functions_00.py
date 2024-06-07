from data_stark import lista_personajes

def validar_lista(lista:list)-> None:
    """RECICLABLE: Verifica si el usuario ingreso una lista

    Args:
        lista (list): lista a verificar

    Raises:
        TypeError: Si el usuario no paso una lista, lanza una excepción
    """
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")

def convertir_numeros(lista: list) -> list:
    """RECICLABLE: Convierte los valores que contienen números a tipo float, eliminando las comillas.

    Args:
        lista (list): Lista de diccionarios donde se realizará la conversión.

    Returns:
        list: La misma lista con los valores que son números convertidos a tipo float.
    """
    validar_lista(lista)
    
    for personaje in lista:
        for clave, valor in personaje.items():
            if valor.replace('.', '', 1).isdigit():
                personaje[clave] = float(valor)
    return lista

convertir_numeros(lista_personajes)

def cuadro_heroes(lista:list)-> None:
    """Imprime una cuadro de superhéroes con columnas que organizan su información.

    Args:
        lista (list): Lista de superhéroes que recibe la funcion mostrar_heroe() para imprimir. Tambien indica la cantidad de veces que iterara la funcion mostar_heroe()
    """
    validar_lista(lista)
    print("                                                                                       LISTA DE HEROES")
    print("        Nombre                     Identidad                  Empresa        Altura       Peso     Genero               Color de ojos     Color de pelo       Fuerza     Intelgencia")
    print(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    for i in range(len(lista)):
        mostrar_heroe(lista[i])
    print()

def mostrar_heroe(un_heroe: dict)-> None:
    """Imprime la informacion de un superhéroe.

    Args:
        un_heroe (dict): Diccionario que contiene los atributos de un héroe.
    """
    print(f" {un_heroe["nombre"]:>18}     {un_heroe["identidad"]:>29}      {un_heroe["empresa"]:>13}     {un_heroe["altura"]:>6.2f}     {un_heroe["peso"]:>6.2f}       {un_heroe["genero"]:>1}        {un_heroe["color_ojos"]:>23}     {un_heroe["color_pelo"]:>13}       {un_heroe["fuerza"]:>6.2f}         {un_heroe["inteligencia"]:>7}")

def obtener_datos(lista, campo)->list:
    """RECICLABLE: Obtiene datos especificos dentro de una lista

    Args:
        lista (_type_): lista donde se ubican los datos
        campo (_type_): key donde se ubica el dato que queremos obtener

    Returns:
        _type_: Retorna una lista con los datos solicitados por el usuario
    """
    validar_lista(lista)
    
    datos = [personaje[campo] for personaje in lista]
    return datos

def mostrar_datos(lista, campo)-> None:
    """RECICLABLE: Imprime los datos que solicita el usuario con la funcion obtener_datos_personaje

    Args:
        lista (_type_): lista donde se ubican los datos
        campo (_type_): key donde se ubica el dato que queremos obtener
    """
    validar_lista(lista)
    datos = obtener_datos(lista, campo)
    for dato in datos:
        print(f"{campo.capitalize()}: {dato}")

def mostrar_nombre_y_alutra(lista:list)-> None:
    """Imprime el nombre y la altura de cada superhéroe

    Args:
        lista (list): Lista donde se encuentran los datos
    """
    for personaje in lista:
        print(f"Nombre: {personaje['nombre']} - Altura: {personaje["altura"]}cm")

def obtener_minmax(lista: list, maxmin: str, campo: str) -> tuple:
    """RECICLABLE: Obtiene el minimo o el maximo de algun key dentro de un dict

    Args:
        lista (list): lista que contiene dicts
        maxmin (str): maximo("max") o minimo("min")
        campo (str): keys donde se va a trabajar

    Raises:
        ValueError: Si el usuario no pasa ni "max" ni "min"

    Returns:
        tuple: Tupla con los datos obtenidos
    """
    validar_lista(lista)
    
    nombre = lista[0]['nombre']
    valor = float(lista[0][campo])
    
    if maxmin == "max":
        for elemento in lista:
            valor_elemento = float(elemento[campo])
            if valor_elemento > valor:
                valor = valor_elemento
                nombre = elemento["nombre"]
    elif maxmin == "min":
        for elemento in lista:
            valor_elemento = float(elemento[campo])
            if valor_elemento < valor:
                valor = valor_elemento
                nombre = elemento["nombre"]
    else:
        raise ValueError("Error. Se calculan minimos y maximos")
    return nombre, valor

def calcular_promedio_campos(lista:list, campo:str)-> float:
    """RECICLABLE: Calcula promedios de todos los values de un key en una lista diccionarios

    Args:
        lista (list): lista de diccionarios donde se buscarán los valores.
        campo (str): El nombre del campo en los diccionarios donde se buscarán los valores numéricos.

    Returns:
        float: El promedio de los valores encontrados en el campo especificado.
    """
    validar_lista(lista)
    
    suma_valores = 0
    for valor in lista:
        suma_valores = suma_valores + float(valor[campo])
    promedio = suma_valores / len(lista)
    promedio = round(promedio, 2)
    return promedio

def mostrar_info_alturas(lista: list)-> None:
    """Imprime un mensaje indicando la altura promedio de los superhéroes

    Args:
        lista (list): lista donde se buscaran los valores
    """
    altura_maxima = obtener_minmax(lista, "max","altura")
    altura_minima = obtener_minmax(lista, "min", "altura")
    promedio = calcular_promedio_campos(lista, "altura")
    for personaje in lista:
        if personaje["nombre"] == altura_maxima[0]:
            identidad_max = personaje["identidad"]
            
        if personaje["nombre"] == altura_minima[0]:
            identidad_min = personaje["identidad"]
    msj = f'El superhéroe mas alto es: {identidad_max}, alias "{altura_maxima[0]}": {altura_maxima[1]}cm\nEl superhéroe mas bajo es: {identidad_min}, alias "{altura_minima[0]}": {altura_minima[1]}cm\nLa altura promedio de todos los superhéroes es: {promedio}cm'
    print(msj)

def mostar_maxmin_pesos(lista: list)-> None:
    """Imprime el nombre del superhéroe mas pesado y del mas liviano

    Args:
        lista (list): Lista donde se compararan los pesos
    """
    validar_lista(lista)
    max = obtener_minmax(lista, "max", "peso")
    min = obtener_minmax(lista, "min", "peso")
    msj = f"El superhéroe más pesado es {max[0]} con {max[1]}kg, y el mas liviano es {min[0]} con {min[1]}kg"
    print(msj)