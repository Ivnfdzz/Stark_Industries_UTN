from herramientas.functions_00 import *
from herramientas.functions_01 import *
from os import system

def menu():
    """Muestra el menu de opciones

    Returns:
        Retorna un imput donde le pide al usuario que coloque una opción
    """
    system("cls")
    print(f"""
DATA STARK:
Desafio 00:
A. Mostrar la informacion de todos los superhéroes
B. Mostrar el nombre de todos los superhéroes.
C. Mostrar el nombre y altura de todos los superhéroes.
D. Mostrar el superhéroe mas alto, el mas bajo y el promedio de alturas.
E. Mostrar el superhéroe mas pesado y el mas liviano.

Desafio 01:
F. Mostrar el nombre de todos los superéroes (M).
G. Mostrar el nombre de todas las superéroinas (F).
H. Mostrar la informacion de altura de ambos generos por separado
I. Mostrar todos los superhéroes agrupados por color de ojos
J. Mostrar todos los superhéroes agrupados por color de pelo
K. Mostrar todos los superhéroes agrupados por inteligencia
X. Salir de la aplicación
""")
    return input("Seleccione una opción: ").upper()

while True:
    match menu():
        case "A":
            cuadro_heroes(lista_personajes)
        
        case "B":
            mostrar_datos(lista_personajes, "nombre")
        
        case "C":
            mostrar_nombre_y_alutra(lista_personajes)
        
        case "D":
            mostrar_info_alturas(lista_personajes)
        
        case "E":
            mostar_maxmin_pesos(lista_personajes)
        
        case "F":
            mostrar_por_generos(lista_personajes, "M")
        
        case "G":
            mostrar_por_generos(lista_personajes, "F")
        
        case "H":
            case_h()
        
        case "I":
            case_i()
        
        case "J":
            case_j()
        
        case "K":
            case_k()
        
        case "X":
            break
        
        case _:
            print("ERROR: Opción invalida")
        
    system("pause")
    
print("Fin del programa.")