import unittest
import sys
import os

# Agregar directorio actual para encontrar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from crear_tarea import crear_tarea


class TestCrearTarea(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.proyectos = {
            "1": {
                "Nombre": "Proyecto1",
                "Descripcion": "Descripción del proyecto",
                "FechaLimite": 20250630,
                "Tareas": {}
            }
        }
        self.salida = []
    
    def test_crear_tarea_exitosa(self):
        """Test: Crear una tarea exitosamente"""
        args = ["crear_tarea", "Proyecto1", "Tarea1", "Hacer obligatorio", "Ricardo Melendez", "20250615", "PENDIENTE"]
        
        # Simular sin guardar archivo
        import manejoJson
        guardar_original = manejoJson.guardar_proyectos
        manejoJson.guardar_proyectos = lambda x: None
        
        crear_tarea(args, self.proyectos, self.salida)
        
        manejoJson.guardar_proyectos = guardar_original
        
        # Verificaciones
        tareas = self.proyectos["1"]["Tareas"]
        self.assertEqual(len(tareas), 1)
        self.assertTrue("1" in tareas)
        
        tarea = tareas["1"]
        self.assertEqual(tarea["Nombre"], "Tarea1")
        self.assertEqual(tarea["Descripcion"], "Hacer obligatorio")
        self.assertEqual(tarea["Responsable"], "Ricardo Melendez")
        self.assertEqual(tarea["FechaLimite"], "20250615")
        self.assertEqual(tarea["Estado"], "PENDIENTE")
        
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("creada con éxito" in self.salida[0])
    
    def test_crear_tarea_proyecto_no_existe(self):
        """Test: Error al crear tarea en proyecto inexistente"""
        args = ["crear_tarea", "ProyectoInexistente", "Tarea1", "Descripción", "Usuario", "20250615", "PENDIENTE"]
        
        crear_tarea(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos["1"]["Tareas"]), 0)  # No debe crear tarea
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: El proyecto 'ProyectoInexistente' no existe" in self.salida[0])
    
    def test_crear_tarea_nombre_duplicado(self):
        """Test: Error al crear tarea con nombre duplicado (requerido por obligatorio)"""
        # Tarea existente
        self.proyectos["1"]["Tareas"]["1"] = {
            "Nombre": "Tarea1",
            "Descripcion": "Descripción",
            "Responsable": "Usuario",
            "FechaLimite": 20250615,
            "Estado": "PENDIENTE"
        }
        
        args = ["crear_tarea", "Proyecto1", "Tarea1", "Nueva descripción", "Otro Usuario", "20250620", "PENDIENTE"]
        
        crear_tarea(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos["1"]["Tareas"]), 1)  # No debe crear nueva tarea
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Ya existe una tarea con el nombre 'Tarea1'" in self.salida[0])
    
    def test_crear_tarea_fecha_posterior_proyecto(self):
        """Test: Error por fecha de tarea posterior a la fecha del proyecto"""
        args = ["crear_tarea", "Proyecto1", "Tarea1", "Descripción", "Usuario", "20250701", "PENDIENTE"]
        # Fecha proyecto: 20250630, Fecha tarea: 20250701 (posterior)
        
        crear_tarea(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos["1"]["Tareas"]), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: La fecha de la tarea no puede ser posterior a la fecha límite del proyecto" in self.salida[0])
    
    def test_crear_tarea_estado_valido(self):
        """Test: Crear tarea con estados válidos (PENDIENTE, EN_PROGRESO, COMPLETADA)"""
        estados_validos = ["PENDIENTE", "EN_PROGRESO", "COMPLETADA"]
        
        for i, estado in enumerate(estados_validos, 1):
            proyectos_test = {
                "1": {
                    "Nombre": "Proyecto1",
                    "Descripcion": "Descripción del proyecto",
                    "FechaLimite": 20250630,
                    "Tareas": {}
                }
            }
            salida_test = []
            
            args = ["crear_tarea", "Proyecto1", f"Tarea{i}", "Descripción", "Usuario", "20250615", estado]
            
            import manejoJson
            guardar_original = manejoJson.guardar_proyectos
            manejoJson.guardar_proyectos = lambda x: None
            
            crear_tarea(args, proyectos_test, salida_test)
            
            manejoJson.guardar_proyectos = guardar_original
            
            # Verificaciones
            tarea = proyectos_test["1"]["Tareas"]["1"]
            self.assertEqual(tarea["Estado"], estado)
            self.assertTrue("creada con éxito" in salida_test[0])
    
    def test_crear_tarea_estado_invalido(self):
        """Test: Error por estado inválido"""
        args = ["crear_tarea", "Proyecto1", "Tarea1", "Descripción", "Usuario", "20250615", "ESTADO_INVALIDO"]
        
        crear_tarea(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos["1"]["Tareas"]), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: el estado debe ser EN_PROGRESO, COMPLETADA o PENDIENTE" in self.salida[0])
    
    def test_crear_tarea_fecha_invalida(self):
        """Test: Error por fecha con formato inválido"""
        args = ["crear_tarea", "Proyecto1", "Tarea1", "Descripción", "Usuario", "2025-06-15", "PENDIENTE"]
        
        crear_tarea(args, self.proyectos, self.salida)
        
        # Verificaciones
        self.assertEqual(len(self.proyectos["1"]["Tareas"]), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Fecha límite inválida. Usa formato AAAAMMDD" in self.salida[0])
    
    def test_crear_tarea_faltan_argumentos(self):
        """Test: Error por falta de argumentos"""
        args = ["crear_tarea", "Proyecto1", "Tarea1"]  # Faltan argumentos
        
        crear_tarea(args, self.proyectos, self.salida)
        
        self.assertEqual(len(self.proyectos["1"]["Tareas"]), 0)
        self.assertEqual(len(self.salida), 1)
        self.assertTrue("Error: Faltan argumentos" in self.salida[0])


if __name__ == '__main__':
    unittest.main()