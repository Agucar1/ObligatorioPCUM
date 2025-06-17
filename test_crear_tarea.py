import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crear_tarea import crear_tarea


def test_crear_tarea_basico():
    """Test: Crear tarea con nombre, descripción, responsable, fecha y estado"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "FechaLimite": "2025-06-30",
            "Tareas": {}
        }
    }
    salida = []
    
    import manejoJson
    manejoJson.guardar_proyectos = lambda x: None
    
    args = ["crear_tarea", "Proyecto1", "Tarea1", "Descripción", "Juan", "2025-06-15", "PENDIENTE"]
    crear_tarea(args, proyectos, salida)
    
    tarea = proyectos["1"]["Tareas"]["1"]
    assert tarea["Nombre"] == "Tarea1"
    assert tarea["Descripcion"] == "Descripción"
    assert tarea["Responsable"] == "Juan"
    assert tarea["FechaLimite"] == "2025-06-15"
    assert tarea["Estado"] == "PENDIENTE"
    
    print("Crear tarea básico")


def test_no_repetir_nombre():
    """Test: No se puede repetir nombre de tarea en el mismo proyecto"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "FechaLimite": "2025-06-30",
            "Tareas": {
                "1": {"Nombre": "Tarea1"}
            }
        }
    }
    salida = []
    
    args = ["crear_tarea", "Proyecto1", "Tarea1", "Otra desc", "Ana", "2025-06-20", "PENDIENTE"]
    crear_tarea(args, proyectos, salida)
    
    assert len(proyectos["1"]["Tareas"]) == 1 
    assert "Ya existe una tarea con el nombre 'Tarea1'" in salida[0]
    
    print("No repetir nombre")


def test_fecha_no_superar_proyecto():
    """Test: Fecha de tarea no puede superar fecha del proyecto"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "FechaLimite": "2025-06-30",  
            "Tareas": {}
        }
    }
    salida = []
    
    args = ["crear_tarea", "Proyecto1", "Tarea1", "Desc", "Luis", "2025-07-01", "PENDIENTE"]  
    crear_tarea(args, proyectos, salida)
    
    assert len(proyectos["1"]["Tareas"]) == 0 
    assert "no puede ser posterior" in salida[0]
    
    print("Fecha no superar proyecto")


def test_estados_validos():
    """Test: Estados PENDIENTE, EN_PROGRESO, COMPLETADA"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "FechaLimite": "2025-06-30",
            "Tareas": {}
        }
    }
    
    import manejoJson
    manejoJson.guardar_proyectos = lambda x: None
    
    estados = ["PENDIENTE", "EN_PROGRESO", "COMPLETADA"]
    for estado in estados:
        proyectos["1"]["Tareas"] = {} 
        salida = []
        
        args = ["crear_tarea", "Proyecto1", "Tarea1", "Desc", "User", "2025-06-15", estado]
        crear_tarea(args, proyectos, salida)
        
        assert proyectos["1"]["Tareas"]["1"]["Estado"] == estado
    
    print("Estados válidos")


def ejecutar_tests():
    print("=== TESTS CREAR TAREA ===\n")

    try:
        test_crear_tarea_basico()
        test_no_repetir_nombre()
        test_fecha_no_superar_proyecto()
        test_estados_validos()
    except Exception as e:
        print(f"\n ERROR: {e}")


if  __name__ == '__main__':
    ejecutar_tests()