import os
from guardar_salida_en_txt import guardar_salida_en_txt

def limpiar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)

def test_guardar_salida_basica():
    salida = ["Línea 1", "Línea 2", "Línea 3"]
    archivo = "test_salida.txt"
    limpiar_archivo(archivo)

    guardar_salida_en_txt(salida, archivo)

    assert os.path.exists(archivo)
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    assert "Línea 1" in contenido
    assert "Línea 2" in contenido
    assert "Línea 3" in contenido

    print("test_guardar_salida_basica: OK")
    limpiar_archivo(archivo)

def test_guardar_salida_vacia():
    salida = []
    archivo = "test_salida.txt"
    limpiar_archivo(archivo)

    guardar_salida_en_txt(salida, archivo)

    assert os.path.exists(archivo)
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    assert contenido == ""

    print("test_guardar_salida_vacia: OK")
    limpiar_archivo(archivo)

def test_guardar_salida_una_linea():
    salida = ["Una sola línea"]
    archivo = "test_salida.txt"
    limpiar_archivo(archivo)

    guardar_salida_en_txt(salida, archivo)

    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    assert len(lineas) == 1
    assert lineas[0].strip() == "Una sola línea"

    print("test_guardar_salida_una_linea: OK")
    limpiar_archivo(archivo)

def test_guardar_salida_por_defecto():
    salida = ["Texto por defecto"]
    archivo = "salida.txt"
    limpiar_archivo(archivo)

    guardar_salida_en_txt(salida)

    assert os.path.exists(archivo)
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    assert "Texto por defecto" in contenido

    print("test_guardar_salida_por_defecto: OK")
    limpiar_archivo(archivo)

 

def ejecutar_tests():
    print("=== TESTS SALIDA ===\n")

    try:
        test_guardar_salida_basica()
        test_guardar_salida_vacia()
        test_guardar_salida_una_linea()
        test_guardar_salida_por_defecto()
    except Exception as e:
        print(f"\n ERROR: {e}")

if __name__ == "__main__":
    ejecutar_tests()