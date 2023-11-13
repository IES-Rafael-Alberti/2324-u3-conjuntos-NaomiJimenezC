def test_mostrar_nombres_alumnos():
    alumnos_primaria = {"Naomi","Noemi","Nao","Noe"}
    alumno_secundaria = {"Juan","Pepe","Sachi","Salchi","Noe"}

    assert len(sacar_nombres_primaria_y_secundaria(alumnos_primaria,alumno_secundaria)) == 8