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
    while len(nombre_introducido.strip()) != 1 or nombre_introducido.isalpha() != True:
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
#Salida

if __name__ == "__main__":
    #Entrada
    #Procesado
    #Salida
    print()
