"""
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
    Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
    Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
    Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

"""

#Procesado
def obtener_todas_las_frutas(frutas1:set,frutas2:set)->set:
    """Une las dos listas de frutas

    :param frutas1: Primera colección de frutas
    :param frutas2: Segunda Colección de frutas
    :return: Devuelve todas los tipos de frutas disponibles
    """
    return frutas1 | frutas2

def obtener_frutas_unicas(coleccion_frutas_a_comparar:set,coleccion_fruta_comparada:set)->set:
    """
    Obtienes las frutas únicas de una colección de fruta frente a otra

    :param coleccion_frutas_a_comparar: Colección de la que queremos sacar la exclusividad
    :param coleccion_fruta_comparada: Colección con la que queremos comparar la otra colección
    :return: Devuelve las frutas únicas de la colección que quisimos
    """
    return coleccion_frutas_a_comparar - coleccion_fruta_comparada
#Salida

def mostrar_todas_las_frutas(todas_las_frutas:set)->str:
    mensaje_con_todas_las_frutas = "Aquí está toda nuestras frutas: "

    for fruta in todas_las_frutas:
        mensaje_con_todas_las_frutas += fruta +","
    
    return mensaje_con_todas_las_frutas

def mostrar_frutas_unicas(frutas_unicas:set)->str:
    mensaje_frutas_unicas = f"Las frutas únicas de la colección son "
    
    for fruta_unica in frutas_unicas:
        mensaje_frutas_unicas += fruta_unica +","
    
    return mensaje_frutas_unicas

if __name__ == "__main__":
    #Entrada
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    #Procesado
    
    todas_las_frutas = obtener_todas_las_frutas(set_frutas1,set_frutas2)
    frutas_unicas_set_1 = obtener_frutas_unicas(set_frutas1,set_frutas2)
    frutas_unicas_set_2 = obtener_frutas_unicas(set_frutas2,set_frutas1)
    
    #Salida
    
    mensaje_con_todas_las_frutas = mostrar_todas_las_frutas(todas_las_frutas)
    mensaje_frutas_unicas_set_1 = mostrar_frutas_unicas(frutas_unicas_set_1)
    mensaje_frutas_unicas_set_2 = mostrar_frutas_unicas(frutas_unicas_set_2)
    
    print(mensaje_con_todas_las_frutas + "\n" + mensaje_frutas_unicas_set_1 +"\n" + mensaje_frutas_unicas_set_2)