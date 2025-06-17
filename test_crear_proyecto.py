import sys
import os
import manejoJson

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crear_proyecto import crear_proyecto


def get_proyectos():
    return {}


def test_crear_proyecto_exitoso():
    proyectos = get_proyectos()
    salida = []
    args = ["crear_proyecto", "Proyecto1", "Descripción del proyecto", "20250630"]
    
    guardar_original = manejoJson.guardar_proyectos
    manejoJson.guardar_proyectos = lambda x: None

    crear_proyecto(args, proyectos, salida)

    manejoJson.guardar_proyectos = guardar_original

    assert len(proyectos) == 1
    assert proyectos["1"]["Nombre"] == "Proyecto1"
    assert proyectos["1"]["Descripcion"] == "Descripción del proyecto"
    assert proyectos["1"]["FechaLimite"] == "20250630"
    assert "creado con éxito" in salida[0]
    print("test_crear_proyecto_exitoso pasó")


def test_crear_segundo_proyecto_id_incremental():
    proyectos = {
        "1": {
            "Nombre": "Proyecto Existente",
            "Descripcion": "Descripción",
            "FechaLimite": "20250630",
            "Tareas": {}
        }
    }
    salida = []
    args = ["crear_proyecto", "Proyecto2", "Segunda descripción", "20250715"]

    
    guardar_original = manejoJson.guardar_proyectos
    manejoJson.guardar_proyectos = lambda x: None

    crear_proyecto(args, proyectos, salida)

    manejoJson.guardar_proyectos = guardar_original

    assert len(proyectos) == 2
    assert "2" in proyectos
    assert proyectos["2"]["Nombre"] == "Proyecto2"
    assert "ID 2" in salida[0]
    print("test_crear_segundo_proyecto_id_incremental pasó")


def test_crear_proyecto_nombre_duplicado():
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "Descripcion": "Descripción",
            "FechaLimite": "2025-06-30",
            "Tareas": {}
        }
    }
    salida = []
    args = ["crear_proyecto", "Proyecto1", "Nueva descripción", "20250715"]

    crear_proyecto(args, proyectos, salida)

    assert len(proyectos) == 1  # No se debe agregar nada
    assert "Ya existe un proyecto con el nombre" in salida[0]
    print("test_crear_proyecto_nombre_duplicado pasó")


def test_crear_proyecto_faltan_argumentos():
    proyectos = get_proyectos()
    salida = []
    args = ["crear_proyecto", "Proyecto1"]

    crear_proyecto(args, proyectos, salida)

    assert len(proyectos) == 0
    assert "Error: Faltan argumentos" in salida[0]
    print("test_crear_proyecto_faltan_argumentos pasó")

    
def ejecutar_tests(): #Ejecucion de los tests captura error
    print("=== TESTS CREAR PROYECTO ===\n")

    try:
        test_crear_proyecto_exitoso()
        test_crear_segundo_proyecto_id_incremental()
        test_crear_proyecto_nombre_duplicado()
        test_crear_proyecto_faltan_argumentos()
    except Exception as e:
        print(f"\n ERROR: {e}")

if __name__ == "__main__":
    ejecutar_tests()