import unittest
import sys
import os

# Agregar directorio actual para encontrar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from listar_proyectos import listar_proyectos


class TestListarProyectos(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.salida = []
    
    def test_listar_proyectos_vacio(self):
        """Test: Listar cuando no hay proyectos"""
        proyectos = {}
        
        resultado = listar_proyectos(proyectos, self.salida)
        
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0], "No hay proyectos guardados.")
    
    def test_listar_un_proyecto_basico(self):
        """Test: Listar un proyecto básico"""
        proyectos = {
            "1": {
                "Nombre": "Proyecto1",
                "Descripcion": "Descripción del proyecto",
                "FechaLimite": "2025-06-30",
                "Tareas": {}
            }
        }
        
        resultado = listar_proyectos(proyectos, self.salida)
        
        # Verificaciones 
        self.assertTrue(any("=== Proyectos ===" in linea for linea in resultado))
        self.assertTrue(any("Proyecto: 1" in linea for linea in resultado))
        self.assertTrue(any("Nombre: Proyecto1" in linea for linea in resultado))
    
    def test_listar_proyecto_con_tarea(self):
        """Test: Listar proyecto con una tarea"""
        proyectos = {
            "1": {
                "Nombre": "Proyecto1",
                "Descripcion": "Descripción",
                "FechaLimite": "2025-06-30",
                "Tareas": {
                    "1": {
                        "Nombre": "Tarea1",
                        "Responsable": "Ricardo Melendez",
                    }
                }
            }
        }
        
        resultado = listar_proyectos(proyectos, self.salida)
        
        self.assertTrue(any("Tarea1" in linea and "Ricardo Melendez" in linea for linea in resultado))
    
    def test_retorno_es_lista(self):
        """Test: Verificar que retorna una lista"""
        proyectos = {"1": {"Nombre": "Test", "Descripcion": "Test", "FechaLimite": "20250630", "Tareas": {}}}
        
        resultado = listar_proyectos(proyectos, self.salida)
        
        self.assertIsInstance(resultado, list)
        self.assertTrue(len(resultado) > 0)


if __name__ == '__main__':
    unittest.main()