import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from actualizar_tarea import actualizar_tarea


def get_proyectos():
    return {
        "1": {
            "Nombre": "Proyecto1",
            "Descripcion": "Descripción del proyecto",
            "FechaLimite": "2025-06-30",
            "Tareas": {
                "1": {
                    "Nombre": "Tarea1",
                    "Descripcion": "Hacer obligatorio",
                    "Responsable": "Ricardo Melendez",
                    "FechaLimite": "2025-06-15",
                    "Estado": "PENDIENTE"
                },
                "2": {
                    "Nombre": "Tarea2",
                    "Descripcion": "Estudiar parcial",
                    "Responsable": "María López",
                    "FechaLimite": "2025-06-20",
                    "Estado": "EN_PROGRESO"
                }
            }
        }
    }


def test_actualizar_tarea_exitoso(): # Actualizar tarea exitosamente a EN_PROGRESO
    proyectos = get_proyectos()
    salida = []
    args = ["actualizar_tarea", "Proyecto1", "Tarea1", "EN_PROGRESO"]
    actualizar_tarea(args, proyectos, salida)
    assert proyectos["1"]["Tareas"]["1"]["Estado"] == "EN_PROGRESO"
    assert 'actualizado a "EN_PROGRESO"' in salida[0]
    print("test_actualizar_tarea_exitoso: OK")


def test_actualizar_tarea_a_completada():  # Actualizar tarea exitosamente a COMPLETADO
    proyectos = get_proyectos()
    salida = []
    args = ["actualizar_tarea", "Proyecto1", "Tarea2", "COMPLETADA"]
    actualizar_tarea(args, proyectos, salida)
    assert proyectos["1"]["Tareas"]["2"]["Estado"] == "COMPLETADA"
    assert "COMPLETADA" in salida[0]
    print("test_actualizar_tarea_a_completada: OK")


def test_actualizar_tarea_proyecto_no_existe(): # Actualizar tarea en proyecto inexistente validacion
    proyectos = get_proyectos()
    salida = []
    args = ["actualizar_tarea", "Inexistente", "Tarea1", "EN_PROGRESO"]
    actualizar_tarea(args, proyectos, salida)
    assert "proyecto 'Inexistente' no existe" in salida[0]
    assert proyectos["1"]["Tareas"]["1"]["Estado"] == "PENDIENTE"
    print("test_actualizar_tarea_proyecto_no_existe: OK")


def test_actualizar_tarea_no_existe(): # Actualizar tarea de una inexistente
    proyectos = get_proyectos()
    salida = []
    args = ["actualizar_tarea", "Proyecto1", "TareaInexistente", "EN_PROGRESO"]
    actualizar_tarea(args, proyectos, salida)
    assert "tarea 'TareaInexistente' no existe" in salida[0]
    print("test_actualizar_tarea_no_existe: OK")


def test_actualizar_tarea_estado_invalido(): #Estado de la tarea invalido
    proyectos = get_proyectos()
    salida = []
    args = ["actualizar_tarea", "Proyecto1", "Tarea1", "INVALIDO"]
    actualizar_tarea(args, proyectos, salida)
    assert "Estado inválido" in salida[0]
    assert proyectos["1"]["Tareas"]["1"]["Estado"] == "PENDIENTE"
    print("test_actualizar_tarea_estado_invalido: OK")


def test_actualizar_tarea_proyecto_sin_tareas(): # Proyecto sin tareas
    proyectos = {
        "1": {
            "Nombre": "ProyectoVacio",
            "Tareas": {}
        }
    }
    salida = []
    args = ["actualizar_tarea", "ProyectoVacio", "Tarea1", "EN_PROGRESO"]
    actualizar_tarea(args, proyectos, salida)
    assert "no tiene tareas" in salida[0]
    print("test_actualizar_tarea_proyecto_sin_tareas: OK")


def test_actualizar_tarea_faltan_argumentos(): # no tiene suficientes argumentos la entrada
    proyectos = get_proyectos()
    casos = [
        ["actualizar_tarea"],
        ["actualizar_tarea", "Proyecto1"],
        ["actualizar_tarea", "Proyecto1", "Tarea1"]
    ]
    for args in casos:
        salida = []
        actualizar_tarea(args, proyectos, salida)
        assert "Faltan argumentos" in salida[0]
    print("test_actualizar_tarea_faltan_argumentos: OK")


def test_actualizar_tarea_case_insensitive(): # CASESENSITIVE
    proyectos = get_proyectos()
    salida = []
    args = ["actualizar_tarea", "proyecto1", "tarea1", "completada"]
    actualizar_tarea(args, proyectos, salida)
    assert proyectos["1"]["Tareas"]["1"]["Estado"] == "COMPLETADA"
    assert "actualizado" in salida[0]
    print("test_actualizar_tarea_case_insensitive : OK")
   
    
def ejecutar_tests(): #Ejecucion de los tests captura error
    print("=== TESTS ACTUALIZAR TAREA === \n")

    try:
        test_actualizar_tarea_exitoso()
        test_actualizar_tarea_a_completada()
        test_actualizar_tarea_proyecto_no_existe()
        test_actualizar_tarea_no_existe()
        test_actualizar_tarea_estado_invalido()
        test_actualizar_tarea_proyecto_sin_tareas()
        test_actualizar_tarea_faltan_argumentos()
        test_actualizar_tarea_case_insensitive()
    except Exception as e:
        print(f"\n ERROR: {e}")

if __name__ == "__main__":
    ejecutar_tests()