import json
import os

ARCHIVO_JSON = "proyectos.json"

def cargar_proyectos():
    if os.path.exists(ARCHIVO_JSON): # verifica que nuestro archivo JSON existe en el repositorio
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f: #Si existe lo abre como lectura y su formateo correcto
            return json.load(f) # Lee el archivo y convierte su contenido a diccionarios de python
    else:
        return {}

def guardar_proyectos(proyectos):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f: #abre el archivo en modo escrirtua en su formato correcto
        json.dump(proyectos, f, indent=4, ensure_ascii=False) # Convierte el diccionario de python en texto JSON, le genera el identado y permite guardar caracteres especiales.