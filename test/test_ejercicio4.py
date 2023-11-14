from src.ejercicio4 import obtener_todas_las_frutas,obtener_frutas_unicas

def test_obtener_todas_las_frutas():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    
    assert len(obtener_todas_las_frutas(set_frutas1,set_frutas2)) == 7
    
def test_obtener_frutas_unicas_del_setFrutas1():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    
    assert len(obtener_frutas_unicas(set_frutas1,set_frutas2)) == 2

def test_obtener_frutas_unicas_del_setFrutas1():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    
    assert len(obtener_frutas_unicas(set_frutas2,set_frutas1)) == 2