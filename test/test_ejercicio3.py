from src.ejercicio3 import *


def test_calcular_conjunto_potencia():
    conjunto_prueba = {1,2,3}
    
    assert len(conjunto_potencia(conjunto_prueba)) == 8