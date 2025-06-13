
def guardar_salida_en_txt(salida, nombre_archivo="salida.txt"): # esta funcion guarda en el txt todo lo ingresado en la lista [salida].
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for linea in salida:
            f.write(linea + "\n")