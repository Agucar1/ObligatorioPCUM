import unittest
import sys
import os

# Agregar directorio actual para encontrar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from actualizar_tarea import actualizar_tarea


class TestActualizarTarea(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.proyectos = {
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
        self.salida = []
    
    def test_actualizar_tarea_exitoso(self):
        """Test: Actualizar estado de tarea exitosamente"""
        args = ["actualizar_tarea", "Proyecto1", "Tarea1", "EN_PROGRESO"]
        
        actualizar_tarea(args, self.proyectos, self.salida)
        
        # Verificar que se actualizó el estado
        tarea = self.proyectos["1"]["Tareas"]["1"]
        self.assertEqual(tarea["Estado"], "EN_PROGRESO")
        
        # Verificar mensaje de confirmación
        self.assertEqual(len(self.salida), 1)
        self.assertTrue('Estado de la tarea "Tarea1" actualizado a "EN_PROGRESO"' in self.salida[0])
    
    def test_actualizar_tarea_a_completada(self):
        """Test: Actualizar tarea a COMPLETADA"""
        args = ["actualizar_tarea", "Proyecto1", "Tarea2", "COMPLETADA"]
        
        actualizar_tarea(args, self.proyectos, self.salida)
        
        # Verificar cambio
        tarea = self.proyectos["1"]["Tareas"]["2"]
        self.assertEqual(tarea["Estado"], "COMPLETADA")
        self.assertTrue('"COMPLETADA"' in self.salida[0])
    
    def test_actualizar_tarea_proyecto_no_existe(self):
        """Test: Error al actualizar tarea de proyecto inexistente"""
        args = ["actualizar_tarea", "ProyectoInexistente", "Tarea1", "EN_PROGRESO"]
        
        actualizar_tarea(args, self.proyectos, self.salida)
        
        # Verificar error
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: El proyecto 'ProyectoInexistente' no existe" in self.salida[0])
        
        # Verificar que no se modificó nada
        tarea = self.proyectos["1"]["Tareas"]["1"]
        self.assertEqual(tarea["Estado"], "PENDIENTE")  # Estado original
    
    def test_actualizar_tarea_no_existe(self):
        """Test: Error al actualizar tarea inexistente"""
        args = ["actualizar_tarea", "Proyecto1", "TareaInexistente", "EN_PROGRESO"]
        
        actualizar_tarea(args, self.proyectos, self.salida)
        
        # Verificar error
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: La tarea 'TareaInexistente' no existe en el proyecto 'Proyecto1'" in self.salida[0])
    
    def test_actualizar_tarea_estado_invalido(self):
        """Test: Error por estado inválido"""
        args = ["actualizar_tarea", "Proyecto1", "Tarea1", "ESTADO_INVALIDO"]
        
        actualizar_tarea(args, self.proyectos, self.salida)
        
        # Verificar error
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Estado inválido. Estados válidos:" in self.salida[0])
        
        # Verificar que no se modificó el estado
        tarea = self.proyectos["1"]["Tareas"]["1"]
        self.assertEqual(tarea["Estado"], "PENDIENTE")  # Estado original
    
    def test_actualizar_tarea_proyecto_sin_tareas(self):
        """Test: Error al actualizar en proyecto sin tareas"""
        proyectos_sin_tareas = {
            "1": {
                "Nombre": "ProyectoVacio",
                "Tareas": {}
            }
        }
        args = ["actualizar_tarea", "ProyectoVacio", "Tarea1", "EN_PROGRESO"]
        
        actualizar_tarea(args, proyectos_sin_tareas, self.salida)
        
        # Verificar error
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: El proyecto 'ProyectoVacio' no tiene tareas" in self.salida[0])
    
    def test_actualizar_tarea_faltan_argumentos(self):
        """Test: Error por falta de argumentos"""
        casos_error = [
            ["actualizar_tarea"],
            ["actualizar_tarea", "Proyecto1"],
            ["actualizar_tarea", "Proyecto1", "Tarea1"]
        ]
        
        for args in casos_error:
            salida_test = []
            actualizar_tarea(args, self.proyectos, salida_test)
            
            self.assertEqual(len(salida_test), 1)
            self.assertTrue("Error: Faltan argumentos" in salida_test[0])
    
    def test_actualizar_tarea_case_insensitive(self):
        """Test: Buscar proyecto y tarea sin importar mayúsculas/minúsculas"""
        args = ["actualizar_tarea", "PROYECTO1", "TAREA1", "completada"]
        
        actualizar_tarea(args, self.proyectos, self.salida)
        
        # Verificar que encontró y actualizó (estado se guarda en mayúsculas)
        tarea = self.proyectos["1"]["Tareas"]["1"]
        self.assertEqual(tarea["Estado"], "COMPLETADA")
        self.assertTrue("actualizado" in self.salida[0])


if __name__ == '__main__':
    unittest.main()