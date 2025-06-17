import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from listar_tareas import listar_tareas


def test_listar_todas_las_tareas():
    """Test: Listar todas las tareas sin filtro"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "Tareas": {
                "1": {"Nombre": "Tarea1", "Responsable" : "Agustin","FechaLimite": "2025-06-15","Estado": "PENDIENTE"},
                "2": {"Nombre": "Tarea2", "Responsable" : "Agustin","FechaLimite": "2025-06-15", "Estado": "EN_PROGRESO"},
                "3": {"Nombre": "Tarea3","Responsable" : "Agustin","FechaLimite": "2025-06-15", "Estado": "COMPLETADA"}
            }
        }
    }
    salida = []
    
    args = ["listar_tareas", "Proyecto1"]
    listar_tareas(args, proyectos, salida)
    
    salida_texto = " ".join(salida)
    assert "Tarea1" in salida_texto
    assert "Tarea2" in salida_texto  
    assert "Tarea3" in salida_texto
    assert "Proyecto1" in salida_texto
    
    print("Listar todas las tareas")


def test_listar_tareas_filtro_estado():
    """Test: Listar tareas filtradas por estado"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1", 
            "Tareas": {
                "1": {"Nombre": "Tarea1","Responsable" : "Agustin", "FechaLimite": "2025-06-15","Estado": "PENDIENTE"},
                "2": {"Nombre": "Tarea2","Responsable" : "Agustin", "FechaLimite": "2025-06-15","Estado": "EN_PROGRESO"},
                "3": {"Nombre": "Tarea3","Responsable" : "Agustin", "FechaLimite": "2025-06-15","Estado": "PENDIENTE"}
            }
        }
    }
    salida = []
    
    args = ["listar_tareas", "Proyecto1", "PENDIENTE"]
    listar_tareas(args, proyectos, salida)
    
    salida_texto = " ".join(salida)
    assert "Tarea1" in salida_texto  
    assert "Tarea3" in salida_texto  
    assert "Tarea2" not in salida_texto  
    assert "PENDIENTE" in salida_texto
    
    print("Filtrar por estado")


def test_proyecto_no_existe():
    """Test: Error al listar tareas de proyecto inexistente"""
    proyectos = {
        "1": {"Nombre": "Proyecto1", "Tareas": {}}
    }
    salida = []
    
    args = ["listar_tareas", "ProyectoInexistente"]
    listar_tareas(args, proyectos, salida)
    
    assert "No se encontró el proyecto 'ProyectoInexistente'" in salida[0]
    
    print("✓ Proyecto no existe")


def test_proyecto_sin_tareas():
    """Test: Proyecto sin tareas"""
    proyectos = {
        "1": {"Nombre": "ProyectoVacio", "Tareas": {}}
    }
    salida = []
    
    args = ["listar_tareas", "ProyectoVacio"]
    listar_tareas(args, proyectos, salida)
    
    salida_texto = " ".join(salida)
    assert "no tiene tareas" in salida_texto or "sin tareas" in salida_texto
    
    print("✓ Proyecto sin tareas")


def test_estado_sin_resultados():
    """Test: Filtrar por estado que no tiene tareas"""
    proyectos = {
        "1": {
            "Nombre": "Proyecto1",
            "Tareas": {
                "1": {"Nombre": "Tarea1","Responsable" : "Agustin", "FechaLimite": "2025-06-15", "Estado": "PENDIENTE"}
            }
        }
    }
    salida = []
    
    args = ["listar_tareas", "Proyecto1", "COMPLETADA"]
    listar_tareas(args, proyectos, salida)
    
    salida_texto = " ".join(salida)
    assert "No hay tareas" in salida_texto or "COMPLETADA" in salida_texto
    
    print("✓ Estado sin resultados")


def ejecutar_tests():
    print("=== TESTS LISTAR TAREAS ===\n")
    
    try:
        test_listar_todas_las_tareas()
        test_listar_tareas_filtro_estado()
        test_proyecto_no_existe()
        test_proyecto_sin_tareas()
        test_estado_sin_resultados()
    except Exception as e:
        print(f"\n ERROR: {e}")


if __name__ == "__main__":
    ejecutar_tests()