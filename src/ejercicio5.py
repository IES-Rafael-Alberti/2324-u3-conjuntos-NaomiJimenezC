
"""
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""

#Procesado
def sacar_conjunto_pares(numeros:set)->set:
    """Obtiene los pares de un conjunto de números

    Parameters
    ----------
    numeros : set
        El conjunto de números del que vamos a sacar pares

    Returns
    -------
    set
        El conjunto de números pares
    """
    numeros_pares = set()
    for numero_par in numeros:
        if numero_par % 2 == 0:
            numeros_pares.add(numero_par)
    return numeros_pares

def obtener_multiplos_de_3(numeros:set)->set:
    """Obtengo los multiplos de 3 de un conjunto de números

    Parameters
    ----------
    numeros : set
        El conjunto de números del que vamos a sacar pares


    Returns
    -------
    set
        El conjunto con los múltiplos de 3
    """
    multiplos_de_3 = set()
    for multiplo_3 in numeros:
        if multiplo_3 % 3 == 0:
            multiplos_de_3.add(multiplo_3)
    return multiplos_de_3

def obtener_inteseccion(conjunto_numero1:set,conjunto_numeros2:set)->set:
    """Obtienes la intersección entre dos conjunto de números

    Parameters
    ----------
    conjunto_numero1 : set
        Un conjunto de números
    conjunto_numeros2 : set
        Un conjunto de números

    Returns
    -------
    set
        El conjunto de los elementos comunes entre ambos conjuntos
    """
    return conjunto_numero1 & conjunto_numeros2

#Salida

def mostrar_conjunto(conjunto:set)->str:
    contenido_conjunto = ""

    for numero in conjunto:
        contenido_conjunto+= str(numero) + ","
    
    return contenido_conjunto

if __name__ == "__main__":
    #Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    #Procesado
    conjunto_numeros_pares = sacar_conjunto_pares(numeros)
    multiplos_de_3 = obtener_multiplos_de_3(numeros)
    numeros_en_comun = obtener_inteseccion(conjunto_numeros_pares,multiplos_de_3)
    #Salida

    mensaje_pares = "Los números pares son: " + mostrar_conjunto(conjunto_numeros_pares)
    mensaje_multiplos_3 = "Los multiplos de 3 son: " + mostrar_conjunto(multiplos_de_3)
    mensaje_interseccion = "Los números en común: " + mostrar_conjunto(numeros_en_comun)

    print(mensaje_pares)
    print(mensaje_multiplos_3)
    print(mensaje_interseccion)