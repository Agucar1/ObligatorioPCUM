from crear_proyecto import crear_proyecto
from listar_proyectos import listar_proyectos
from crear_tarea import crear_tarea
from listar_tareas import listar_tareas
import manejoJson 

def procesar_comandos(args):
    salida = []
    proyectos = manejoJson.cargar_proyectos()

    if not args:
        salida.append("No se pasaron argumentos.")
        return salida

    comando = args[0].lower()

    if comando == "crear_proyecto":
        crear_proyecto(args, proyectos, salida)

    elif comando == "listar_proyectos":
       salida = listar_proyectos(proyectos, salida)

    elif comando == "crear_tarea":
        crear_tarea(args, proyectos, salida)

    elif comando == "listar_tareas":
        listar_tareas(args, proyectos, salida)    

    else:
        salida.append(f"Comando no reconocido: '{comando}'")

    return salida