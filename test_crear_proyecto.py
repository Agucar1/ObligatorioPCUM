import unittest
import sys
import os

# Agregar directorio actual para encontrar los módulos del proyecto
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crear_proyecto import crear_proyecto


class TestCrearProyecto(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.proyectos = {}
        self.salida = []
    
    def test_crear_proyecto_exitoso(self):
        """Test: Crear un proyecto exitosamente (requerido por obligatorio)"""
        args = ["crear_proyecto", "Proyecto1", "Descripción del proyecto", "20250630"]
        
        # Simular guardar_proyectos para evitar crear archivos durante tests
        import manejoJson
        guardar_original = manejoJson.guardar_proyectos
        manejoJson.guardar_proyectos = lambda x: None
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        # Restaurar función original
        manejoJson.guardar_proyectos = guardar_original
        
        # Verificar que se creó el proyecto correctamente
        self.assertEqual(len(self.proyectos), 1)
        self.assertEqual(self.proyectos["1"]["Nombre"], "Proyecto1")
        self.assertEqual(self.proyectos["1"]["Descripcion"], "Descripción del proyecto")
        self.assertEqual(self.proyectos["1"]["FechaLimite"], "20250630")
        self.assertTrue("creado con éxito" in self.salida[0])
    
    def test_crear_segundo_proyecto_id_incremental(self):
        """Test: Verificar que se asignan IDs incrementales a los proyectos"""
        # Simular proyecto existente con ID 1
        self.proyectos["1"] = {
            "Nombre": "Proyecto Existente",
            "Descripcion": "Descripción",
            "FechaLimite": "20250630",
            "Tareas": {}
        }
        
        args = ["crear_proyecto", "Proyecto2", "Segunda descripción", "20250715"]
        
        # Simular guardar_proyectos
        import manejoJson
        guardar_original = manejoJson.guardar_proyectos
        manejoJson.guardar_proyectos = lambda x: None
        
        crear_proyecto(args, self.proyectos, self.salida)
        manejoJson.guardar_proyectos = guardar_original
        
        # Verificar que el nuevo proyecto tiene ID 2
        self.assertEqual(len(self.proyectos), 2)
        self.assertTrue("2" in self.proyectos)
        self.assertEqual(self.proyectos["2"]["Nombre"], "Proyecto2")
        self.assertTrue("ID 2" in self.salida[0])
    
    def test_crear_proyecto_nombre_duplicado(self):
        """Test: Error al crear proyecto con nombre duplicado (requerido por obligatorio)"""
        # Crear proyecto existente
        self.proyectos["1"] = {
            "Nombre": "Proyecto1",
            "Descripcion": "Descripción",
            "FechaLimite": "2025-06-30", 
            "Tareas": {}
        }
        
        # Intentar crear proyecto con mismo nombre
        args = ["crear_proyecto", "Proyecto1", "Nueva descripción", "20250715"]
        crear_proyecto(args, self.proyectos, self.salida)
        
        # Verificar que no se creó proyecto duplicado
        self.assertEqual(len(self.proyectos), 1)  # Solo debe haber 1 proyecto
        self.assertTrue("Ya existe un proyecto con el nombre" in self.salida[0])
    
    def test_crear_proyecto_faltan_argumentos(self):
        """Test: Error por falta de argumentos necesarios"""
        args = ["crear_proyecto", "Proyecto1"]  # Faltan descripción y fecha
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        # Verificar que no se creó ningún proyecto
        self.assertEqual(len(self.proyectos), 0)
        self.assertTrue("Error: Faltan argumentos" in self.salida[0])


if __name__ == '__main__':
    unittest.main()