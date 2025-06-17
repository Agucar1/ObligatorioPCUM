import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from listar_proyectos import listar_proyectos

def test_listar_proyectos_vacio():
    salida = []
    proyectos = {}
    resultado = listar_proyectos(proyectos, salida)

    assert isinstance(resultado, list)
    assert len(resultado) == 1
    assert resultado[0] == "No hay proyectos guardados."
    print("test_listar_proyectos_vacio: OK")

def test_listar_un_proyecto_basico():
    salida = []
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "Descripcion": "Descripción del proyecto",
            "FechaLimite": "2025-06-30",
            "Tareas": {}
        }
    }

    resultado = listar_proyectos(proyectos, salida)

    assert isinstance(resultado, list)
    assert any("=== Proyectos ===" in linea for linea in resultado)
    assert any("Proyecto: 1" in linea for linea in resultado)
    assert any("Nombre: Proyecto1" in linea for linea in resultado)
    print("test_listar_un_proyecto_basico: OK")

def test_listar_proyecto_con_tarea():
    salida = []
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "Descripcion": "Descripción",
            "FechaLimite": "2025-06-30",
            "Tareas": {
                "1": {
                    "Nombre": "Tarea1",
                    "Responsable": "Ricardo Melendez"
                }
            }
        }
    }

    resultado = listar_proyectos(proyectos, salida)

    assert any("Tarea1" in linea and "Ricardo Melendez" in linea for linea in resultado)
    print("test_listar_proyecto_con_tarea: OK")

def test_retorno_es_lista():
    salida = []
    proyectos = {
        "1": {
            "Nombre": "Test",
            "Descripcion": "Test",
            "FechaLimite": "20250630",
            "Tareas": {},
        }
    }

    resultado = listar_proyectos(proyectos, salida)

    assert isinstance(resultado, list)
    assert len(resultado) > 0
    print("test_retorno_es_lista: OK")

def ejecutar_tests():
    print("=== TESTS LISTAR PROYECTOS ===\n")

    try:
        test_listar_proyectos_vacio()
        test_listar_un_proyecto_basico()
        test_listar_proyecto_con_tarea()
        test_retorno_es_lista()
    except Exception as e:
        print(f"\n ERROR: {e}")

if __name__ == "__main__":
    ejecutar_tests()