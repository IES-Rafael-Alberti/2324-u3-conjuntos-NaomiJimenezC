""" 
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. 
A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

    Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
    Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
    Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
    Mostrar si todos los nombres de primaria están incluidos en secundaria.

"""

#entrada
def introducir_nombre_pila()->str:
    nombre_introducido = input("Introduce el nombre de pila o introduce x para salir: ")
    while nombre_introducido.isalpha() != True:
        nombre_introducido = input("Introduce el nombre de pila: ")
    return nombre_introducido

#Procesado
def sacar_nombre_primaria_y_secundaria(alumnos_primaria:set,alumnos_secundaria:set)->set:
    """Obtiene todos los nombres de alumnos de primaria y secundaria sin repetición

    Parameters
    ----------
    alumnos_primaria : set
        Conjunto de nombres de alumnos de primaria.
    alumnos_secundaria : set
        Conjunto de nombres de alumnos de secundaria.

    Returns
    -------
    set
        Devuelve el conjunto de nombres de todos los alumnos.
    """
    
    return alumnos_primaria | alumnos_secundaria

def sacar_alumnos_repetidos(alumnos_primaria:set,alumno_secundaria:set)->set:
    """
    sacar_alumnos_repetidos Saca los nombres repetidos en primaria y secundaria

    Se hace una intersección entre los dos conjuntos para sacar los nombres que 
    se repita en ambos conjuntos

    Args:
        alumnos_primaria (set): Conjunto de nombres de primaria
        alumno_secundaria (set): Conjunto de nombbres de secundaria

    Returns:
        set: Devuelve el conjunto de nombres repetidos.
    """
    
    return alumnos_primaria & alumno_secundaria

def sacar_nombres_no_repetidos_en_primaria(alumnos_primaria:set,alumno_secundaria:set)->set:
    """Saca los nombres de alumnos de primaria que no estén en secundaria

    Parameters
    ----------
    alumnos_primaria : set 
        Conjunto de nombres de primaria
    alumnos_secundaria : set 
        Conjunto de nombres de secundaria
    
    Returns
    -------
    Devuelve los nombres de primaria que no estén en secundaria
    
    """
    
    return alumnos_primaria - alumno_secundaria


def comprobar_si_se_repiten_todos_los_nombres(alumnos_primaria:set,alumno_secundaria:set)->bool:
    """Comprueba si los nombres en primaria están todos repetidos en la ESO

    Parameters
    ----------
    alumnos_primaria : set 
        Conjunto de nombres de primaria
    alumnos_secundaria : set 
        Conjunto de nombres de secundaria
    
    Returns
    -------
    Devuelve si todos están repetidos o no
    """
    return alumnos_primaria == alumno_secundaria

#Salida

def mostrar_todos_los_nombres(nombres_alumnos:set)->str:
    todos_los_nombres = "Aquí todos los nombres de los alumnos : "
    
    for nombre in nombres_alumnos:
        todos_los_nombres += nombre +","
    
    return todos_los_nombres

def mostrar_nombres_repetidos(nombres_alumnos_repetidos:set)->str:
    nombres_repetidos = f"Aquí están todos los nombres repetidos: "
    
    for nombre_repetido in nombres_alumnos_repetidos:
        nombres_repetidos += nombre_repetido + ","
    
    return nombres_repetidos

def mostrar_nombres_no_repetidos_de_primaria(nombres_alumnos_no_repetidos:set)->str:
    nombres_de_primaria_no_repetidos = "Estos son los nombres de primaria que no están repetidos: "
    
    for nombre_no_repetido in nombres_alumnos_no_repetidos:
        nombres_de_primaria_no_repetidos += nombre_no_repetido + ","
    
    return nombres_de_primaria_no_repetidos        
    
def mostrar_si_se_repiten_los_nombres_en_primaria_y_la_eso(comprobacion:bool)->str:
    
    if comprobacion:
        return "Se repiten todos los nombres"
    else:
        return "No se repiten todos los nombres"

if __name__ == "__main__":
    #Entrada
    nombres_primaria = set()
    nombres_secundaria = set()
    
    seguir_anadiendo_nombres_primaria = True
    seguir_anadiendo_nombres_secundaria = True
    
    while seguir_anadiendo_nombres_primaria:
        print("Añade los nombres de pila de primaria")
        nombre_pila = introducir_nombre_pila()
        
        if nombre_pila != "x":
            nombres_primaria.add(nombre_pila)
        else:
            seguir_anadiendo_nombres_primaria = False
    
    while seguir_anadiendo_nombres_secundaria:
        print("Añade los nombres de pila de secundaria")
        nombre_pila = introducir_nombre_pila()
        
        if nombre_pila != "x":
            nombres_secundaria.add(nombre_pila)
        else:
            seguir_anadiendo_nombres_secundaria = False
    #Procesado
    
    nombres_primaria_y_eso = sacar_nombre_primaria_y_secundaria(nombres_primaria,nombres_secundaria)
    nombres_repetidos = sacar_alumnos_repetidos(nombres_primaria,nombres_secundaria)
    nombres_no_repetidos = sacar_nombres_no_repetidos_en_primaria(nombres_primaria,nombres_secundaria)
    todos_estan_repetidos= comprobar_si_se_repiten_todos_los_nombres(nombres_primaria,nombres_secundaria)
    
    #Salida
    
    mensaje_nombres_alumnos = mostrar_todos_los_nombres(nombres_primaria_y_eso)
    mensaje_alumnos_repetidos= mostrar_nombres_repetidos(nombres_repetidos)
    mensaje_no_repetidos = mostrar_nombres_no_repetidos_de_primaria(nombres_no_repetidos)
    mensaje_todos_repetidos= mostrar_si_se_repiten_los_nombres_en_primaria_y_la_eso(todos_estan_repetidos)
    
    print(mensaje_nombres_alumnos + "\n" + mensaje_alumnos_repetidos +"\n" + mensaje_no_repetidos + "\n" + mensaje_todos_repetidos)
