from src.ejercicio2 import *
def test_mostrar_nombres_alumnos():
    alumnos_primaria = {"Naomi","Noemi","Nao","Noe"}
    alumno_secundaria = {"Juan","Pepe","Sachi","Salchi","Noe"}

    #uso la longitud para comprobar que todo esté bien porque no sé en que orden está el set
    assert len(sacar_nombre_primaria_y_secundaria(alumnos_primaria,alumno_secundaria)) == 8
    
def test_sacar_nombres_repetidos():
   alumnos_primaria = {"Naomi","Noemi","Nao","Noe"}
   alumno_secundaria = {"Juan","Pepe","Sachi","Salchi","Noe"}
   
   assert len(sacar_alumnos_repetidos(alumnos_primaria,alumno_secundaria)) == 1
   
   
def test_sacar_nombres_de_primaria_no_repetidos_en_secundaria():
    alumnos_primaria = {"Naomi","Noemi","Nao","Noe"}
    alumno_secundaria = {"Juan","Pepe","Sachi","Salchi","Noe"}
    
    assert len(sacar_nombres_no_repetidos_en_primaria(alumnos_primaria,alumno_secundaria)) == 3 
    

def test_comprobar_si_todos_los_nombres_en_primaria_estan_en_secundaria():
    alumnos_primaria = {"Naomi","Noemi","Nao","Noe"}
    alumno_secundaria = {"Naomi","Noemi","Nao","Noe"}
    
    assert(comprobar_si_se_repiten_todos_los_nombres(alumnos_primaria,alumno_secundaria)) == True
    
def test_comprobar_si_todos_los_nombres_en_primaria_no_estan_en_secundaria():
    alumnos_primaria = {"Naomi","Noemi","Nao"}
    alumno_secundaria = {"Naomi","Noemi","Nao","Noe"}
    
    assert(comprobar_si_se_repiten_todos_los_nombres(alumnos_primaria,alumno_secundaria)) == False