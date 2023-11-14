"""
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

    Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
    Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.

"""

#Procesado
def obtener_consonantes(vocales:set)->set:
    """Obtiene una colección de consonantes

    :param vocales: Recibe una colección de vocales
    :type vocales: set
    :return: Una colección de consonantes
    :rtype: set
    """
    abecedario_completo = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    consonantes = set()
        
    for letra in abecedario_completo:
        if letra not in vocales:
            consonantes.add(letra)
        
    return consonantes
    
def recrear_abecedario(vocales:set,consonantes:set)->set:
    """
    recrear_abecedario 

    Recrea el abecedario en base a un set de vocales y de consontantes

    Parameters
    ----------
    vocales : set
        conjunto con las vocales
    consonantes : set
        conjunto con los consonantes

    Returns
    -------
    set
        Devuelve un conjunto del abecedario
    """
    return vocales | consonantes
#Salida

def mostrar_abecedario_recreado(abecedario_recreado:set)->str:

    mensaje_abecedario = "Este es el abecedario recreado: "
    
    for letra in abecedario_recreado:
        mensaje_abecedario += letra +","
    
    return mensaje_abecedario

if __name__ == "__main__":
    #Entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    #Procesado 
    consontantes = obtener_consonantes(vocales)
    letras_comunes = recrear_abecedario(vocales,consontantes)
   
    #Salida
    
    abecedario_reconstruido = mostrar_abecedario_recreado(letras_comunes)
    
    print(abecedario_reconstruido)