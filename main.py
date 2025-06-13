import sys
from guardar_salida_en_txt import guardar_salida_en_txt
from procesar_comandos import procesar_comandos


if __name__ == "__main__":  #llamamos por consola a al archivo main por su nombre
    argumentos = sys.argv[1:] # guardamos el el comando que le pasamos pro consola
    resultado = procesar_comandos(argumentos) # usamos la funcion procesar comandos que verifica el comando a utilizar y ejecuta.
    guardar_salida_en_txt(resultado) # Posterior mente imprimimos lo valore resultantes en el txt
    print("Salida escrita en 'salida.txt'")