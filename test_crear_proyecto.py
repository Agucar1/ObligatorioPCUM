import unittest
from crear_proyecto import crear_proyecto
import sys 
import os
# Aseguramos que el directorio actual esté en el path para importar manejoJson

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestCrearProyecto(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.proyectos = {}
        self.salida = []
    
    def test_crear_proyecto_exitoso(self):
        """Test: Crear un proyecto exitosamente"""
        args = ["crear_proyecto", "Proyecto1", "Descripción del proyecto", "20250630"]
        
        # Simular la función sin guardar en archivo
        import manejoJson
        guardar_original = manejoJson.guardar_proyectos
        manejoJson.guardar_proyectos = lambda x: None  # No hacer nada al guardar
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        # Restaurar función original
        manejoJson.guardar_proyectos = guardar_original
        
        # Verificaciones
        self.assertEqual(len(self.proyectos), 1)
        self.assertTrue("1" in self.proyectos)
        self.assertEqual(self.proyectos["1"]["Nombre"], "Proyecto1")
        self.assertEqual(self.proyectos["1"]["Descripcion"], "Descripción del proyecto")
        self.assertEqual(self.proyectos["1"]["FechaLimite"], 20250630)
        self.assertEqual(self.proyectos["1"]["Tareas"], {})
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("creado con éxito" in self.salida[0])
        self.assertTrue("ID 1" in self.salida[0])
    
    def test_crear_segundo_proyecto_id_incremental(self):
        """Test: Crear segundo proyecto con ID incremental"""
        # Proyecto existente
        self.proyectos["1"] = {
            "Nombre": "Proyecto Existente",
            "Descripcion": "Descripción",
            "FechaLimite": 20250630,
            "Tareas": {}
        }
        
        args = ["crear_proyecto", "Proyecto2", "Segunda descripción", "20250715"]
        
        # Simular sin guardar archivo
        import manejoJson
        guardar_original = manejoJson.guardar_proyectos
        manejoJson.guardar_proyectos = lambda x: None
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        manejoJson.guardar_proyectos = guardar_original
        
        # Verificaciones
        self.assertEqual(len(self.proyectos), 2)
        self.assertTrue("2" in self.proyectos)
        self.assertEqual(self.proyectos["2"]["Nombre"], "Proyecto2")
        self.assertTrue("ID 2" in self.salida[0])
    
    def test_crear_proyecto_nombre_duplicado(self):
        """Test: Error al crear proyecto con nombre duplicado"""
        # Proyecto existente
        self.proyectos["1"] = {
            "Nombre": "Proyecto1",
            "Descripcion": "Descripción",
            "FechaLimite": 20250630,
            "Tareas": {}
        }
        
        args = ["crear_proyecto", "Proyecto1", "Nueva descripción", "20250715"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos), 1)  # No debe crear nuevo proyecto
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Ya existe un proyecto con el nombre" in self.salida[0])
        self.assertTrue("'Proyecto1'" in self.salida[0])
    
    def test_crear_proyecto_nombre_duplicado_mayusculaYminuscula(self):
        """Test: Error con nombre duplicado (mayúsculas/minúsculas)"""
        # Proyecto existente en mayúsculas
        self.proyectos["1"] = {
            "Nombre": "PROYECTO1",
            "Descripcion": "Descripción",
            "FechaLimite": 20250630,
            "Tareas": {}
        }
        
        args = ["crear_proyecto", "proyecto1", "Nueva descripción", "20250715"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos), 1)  # No debe crear nuevo proyecto
        self.assertTrue("Ya existe un proyecto con el nombre" in self.salida[0])
    
    def test_crear_proyecto_faltan_argumentos_nombre(self):
        """Test: Error por falta de nombre"""
        args = ["crear_proyecto"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Faltan argumentos" in self.salida[0])
    
    def test_crear_proyecto_faltan_argumentos_descripcion(self):
        """Test: Error por falta de descripción"""
        args = ["crear_proyecto", "Proyecto1"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Faltan argumentos" in self.salida[0])
    
    def test_crear_proyecto_faltan_argumentos_fecha(self):
        """Test: Error por falta de fecha"""
        args = ["crear_proyecto", "Proyecto1", "Descripción"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Faltan argumentos" in self.salida[0])
    
    def test_crear_proyecto_fecha_invalida_texto(self):
        """Test: Error por fecha con texto"""
        args = ["crear_proyecto", "Proyecto1", "Descripción", "fecha_texto"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Fecha límite debe ser un número entero" in self.salida[0])
    
    def test_crear_proyecto_fecha_invalida_formato_guiones(self):
        """Test: Error por fecha con formato incorrecto (guiones)"""
        args = ["crear_proyecto", "Proyecto1", "Descripción", "2025-06-30"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Fecha límite debe ser un número entero" in self.salida[0])
    
    def test_crear_proyecto_fecha_invalida_decimal(self):
        """Test: Error por fecha con punto decimal"""
        args = ["crear_proyecto", "Proyecto1", "Descripción", "20.25"]
        
        crear_proyecto(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Fecha límite debe ser un número entero" in self.salida[0])


if __name__ == '__main__':
    unittest.main()