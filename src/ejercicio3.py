"""
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]

"""
#Entrada
#Procesado
def conjunto_potencia(s):
    # Inicializa la lista potencia con el conjunto vacío
    potencia = [set()]

    # Itera sobre cada elemento en el conjunto original
    for elemento in s:
        # Itera sobre los conjuntos existentes en la lista potencia
        nuevos_subconjuntos = []
        for subset in potencia:
            # Combina el elemento actual con cada conjunto existente y agrega el nuevo conjunto
            nuevos_subconjuntos.append(subset | {elemento})
        # Agrega los nuevos conjuntos a la lista potencia
        potencia += nuevos_subconjuntos

    return potencia
#Salida

#TODO miralo mañana en clase

if __name__ == "__main__":
prueba = conjunto_potencia({1,2,3})
print(prueba)