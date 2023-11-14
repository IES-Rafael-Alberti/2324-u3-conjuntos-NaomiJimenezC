from src.ejercicio6 import *

def test_obtener_consonantes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    
    assert len(obtener_consonantes(vocales)) == 22
    
def test_recrear_abecedario():
    consontantes = {'q', 'w', 'z', 'y', 'p', 'd', 'f', 'j', 'ñ', 'n', 'g', 'v', 's', 'x', 'm', 'h', 't', 'r', 'b', 'c', 'l', 'k'}
    vocales = {'a', 'e', 'i', 'o', 'u'}
    
    assert len(recrear_abecedario(vocales,consontantes)) == 27