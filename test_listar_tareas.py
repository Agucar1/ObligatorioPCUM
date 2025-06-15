import unittest
import sys
import os

# Agregar directorio actual para encontrar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from listar_tareas import listar_tareas


class TestListarTareas(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.proyectos = {
            "1": {
                "Nombre": "Proyecto1",
                "Descripcion": "Descripción del proyecto",
                "FechaLimite": "20250630",
                "Tareas": {
                    "1": {
                        "Nombre": "Tarea1",
                        "Responsable": "Ricardo Melendez",
                        "Estado": "PENDIENTE"
                    },
                    "2": {
                        "Nombre": "Tarea2",
                        "Responsable": "María López",
                        "Estado": "EN_PROGRESO"
                    },
                    "3": {
                        "Nombre": "Tarea3",
                        "Responsable": "Juan Pérez",
                        "Estado": "PENDIENTE"
                    }
                }
            }
        }
        self.salida = []
    
    def test_listar_todas_las_tareas(self):
        """Test: Listar todas las tareas sin filtro"""
        args = ["listar_tareas", "Proyecto1"]
        
        listar_tareas(args, self.proyectos, self.salida)
        
        # Verificar que muestra todas las tareas
        self.assertTrue(any("Tarea1" in linea for linea in self.salida))
        self.assertTrue(any("Tarea2" in linea for linea in self.salida))
        self.assertTrue(any("Tarea3" in linea for linea in self.salida))
        self.assertTrue(any("=== Tareas del proyecto 'Proyecto1' ===" in linea for linea in self.salida))
    
    def test_listar_tareas_filtro_pendiente(self):
        """Test: Listar solo tareas PENDIENTES"""
        args = ["listar_tareas", "Proyecto1", "PENDIENTE"]
        
        listar_tareas(args, self.proyectos, self.salida)
        
        # Verificar que solo muestra tareas PENDIENTES
        self.assertTrue(any("Tarea1" in linea for linea in self.salida))  # PENDIENTE
        self.assertTrue(any("Tarea3" in linea for linea in self.salida))  # PENDIENTE
        self.assertFalse(any("Tarea2" in linea for linea in self.salida)) # EN_PROGRESO (no deberia aparecer)
        self.assertTrue(any("en estado 'PENDIENTE'" in linea for linea in self.salida))
    
    def test_listar_tareas_filtro_en_progreso(self):
        """Test: Listar solo tareas EN_PROGRESO"""
        args = ["listar_tareas", "Proyecto1", "EN_PROGRESO"]
        
        listar_tareas(args, self.proyectos, self.salida)
        
        # Verificar que solo muestra tareas EN_PROGRESO
        self.assertTrue(any("Tarea2" in linea for linea in self.salida))   # EN_PROGRESO
        self.assertFalse(any("Tarea1" in linea for linea in self.salida))  # PENDIENTE (no deberia aparecer)
        self.assertFalse(any("Tarea3" in linea for linea in self.salida))  # PENDIENTE (no deberia aparecer)
    
    def test_listar_tareas_proyecto_no_existe(self):
        """Test: Error al listar tareas de proyecto inexistente"""
        args = ["listar_tareas", "ProyectoInexistente"]
        
        listar_tareas(args, self.proyectos, self.salida)
        
        self.assertTrue("No se encontró el proyecto 'ProyectoInexistente'" in self.salida[0])
    
    def test_listar_tareas_proyecto_sin_tareas(self):
        """Test: Listar tareas de proyecto sin tareas"""
        proyectos_sin_tareas = {
            "1": {
                "Nombre": "ProyectoVacio",
                "Tareas": {}
            }
        }
        args = ["listar_tareas", "ProyectoVacio"]
        
        listar_tareas(args, proyectos_sin_tareas, self.salida)
        
        self.assertTrue(any("Este proyecto no tiene tareas." in linea for linea in self.salida))
    
    def test_listar_tareas_estado_sin_resultados(self):
        """Test: Filtrar por estado que no tiene tareas"""
        args = ["listar_tareas", "Proyecto1", "COMPLETADA"]
        
        listar_tareas(args, self.proyectos, self.salida)
        
        self.assertTrue(any("No hay tareas en estado 'COMPLETADA'" in linea for linea in self.salida))


if __name__ == '__main__':
    unittest.main()