import crear_proyecto

def procesar_comandos(args): # Procesa que comando se haya ingrsado por consola para realizar accion
    salida = []

    if not args:
        salida.append("No se pasaron argumentos.") # Verifica que se hayan ingresado argumentos
        return salida

    if args[0].lower() == "crear_proyecto": # si el primer parametro ingresado por consola es "crear_proyecto" procede a llamar a la funcion de creacion de proyectos
        crear_proyecto(args, salida)

    
    else:
        salida.append(f"[0] Argumento no reconocido: {args[0]}")

    return salida