from src.ejercicio5 import sacar_conjunto_pares,obtener_multiplos_de_3,obtener_inteseccion

def test_sacar_pares():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    assert len(sacar_conjunto_pares(numeros)) == 5

def test_obtener_multiplos_de_3():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    assert len(obtener_multiplos_de_3(numeros)) == 3

def test_encontrar_interseccion():
    numeros_pares = {2, 4, 6, 8, 10}
    multiplos_de_3 = {3,6,9}

    assert len(obtener_inteseccion(numeros_pares,multiplos_de_3)) == 1