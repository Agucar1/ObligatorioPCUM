import unittest
import sys
import os

# Agregar directorio actual para encontrar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from guardar_salida_en_txt import guardar_salida_en_txt


class TestGuardarSalidaEnTxt(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        # Archivo de prueba que se puede eliminar después
        self.archivo_prueba = "test_salida.txt"
    
    def tearDown(self):
        """Limpiar archivos de prueba después de cada test"""
        if os.path.exists(self.archivo_prueba):
            os.remove(self.archivo_prueba)
        if os.path.exists("salida.txt"):
            os.remove("salida.txt")
    
    def test_guardar_salida_basica(self):
        """Test: Guardar salida básica en archivo"""
        salida = ["Línea 1", "Línea 2", "Línea 3"]
        
        guardar_salida_en_txt(salida, self.archivo_prueba)
        
        # Verificar que se creó el archivo
        self.assertTrue(os.path.exists(self.archivo_prueba))
        
        # Leer el archivo y verificar contenido
        with open(self.archivo_prueba, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Verificar que contiene las líneas esperadas
        self.assertIn("Línea 1", contenido)
        self.assertIn("Línea 2", contenido)
        self.assertIn("Línea 3", contenido)
    
    def test_guardar_salida_vacia(self):
        """Test: Guardar lista vacía"""
        salida = []
        
        guardar_salida_en_txt(salida, self.archivo_prueba)
        
        # Verificar que se creó el archivo
        self.assertTrue(os.path.exists(self.archivo_prueba))
        
        # Verificar que está vacío
        with open(self.archivo_prueba, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        self.assertEqual(contenido, "")
    
    def test_guardar_salida_nombre_archivo_por_defecto(self):
        """Test: Usar nombre de archivo por defecto"""
        salida = ["Test archivo por defecto"]
        
        # No especificar nombre de archivo
        guardar_salida_en_txt(salida)
        
        # Verificar que se creó "salida.txt"
        self.assertTrue(os.path.exists("salida.txt"))
        
        # Verificar contenido
        with open("salida.txt", "r", encoding="utf-8") as f:
            contenido = f.read()
        
        self.assertIn("Test archivo por defecto", contenido)
    
    def test_guardar_salida_una_linea(self):
        """Test: Guardar una sola línea"""
        salida = ["Una sola línea"]
        
        guardar_salida_en_txt(salida, self.archivo_prueba)
        
        # Verificar contenido exacto
        with open(self.archivo_prueba, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        
        self.assertEqual(len(lineas), 1)
        self.assertEqual(lineas[0].strip(), "Una sola línea")


if __name__ == '__main__':
    unittest.main()