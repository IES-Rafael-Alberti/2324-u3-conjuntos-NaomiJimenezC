"""
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]

"""
#Procesado

def conjunto_potencia(conjunto_introducido:set)->list:
    """Calcula el conjunto potencia de un set introducido
    Parameters
    ----------
    conjunto_introducido : set
        Es el conjunto del que queremos obtener su conjunto introducido

    Returns
    -------
    list
        Devuelve una lista con el conjunto potencia calculado
    """
    lista_de_potencias = [set()]
    
    for elemento in conjunto_introducido:
        nuevos_subconjuntos = []
        for subset in lista_de_potencias:
            nuevos_subconjuntos.append(subset | {elemento})
        lista_de_potencias += nuevos_subconjuntos

    return lista_de_potencias
#Salida

def mostrar_conjunto_potencia(conjunto_potencia_calculado:list)->str:
    return f"El conjunto potencia calculado es: {conjunto_potencia_calculado}"

if __name__ == "__main__":
    #Entrada
    conjunto_numerico = {6, 1, 4}
    #Procesado
    conjunto_potencia = conjunto_potencia(conjunto_numerico)
    #Salida
    mensaje_conjunto_potencia = mostrar_conjunto_potencia(conjunto_potencia)
    print(mensaje_conjunto_potencia)