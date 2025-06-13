import sys
import guardar_salida_en_txt
import procesar_comandos


if __name__ == "__main__":  
    argumentos = sys.argv[1:]
    resultado = procesar_comandos(argumentos)
    guardar_salida_en_txt(resultado)
    print("Salida escrita en 'salida.txt'")