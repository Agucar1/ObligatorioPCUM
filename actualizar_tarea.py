import manejoJson

def actualizar_tarea(args, proyectos, salida):
    """Actualiza el estado de una tarea específica en un proyecto
    args: [comando, nombre_proyecto, nombre_tarea, nuevo_estado]
    """
    try:
        # Validamos que se proporcionen los argumentos necesarios
        if len(args) < 4:
            salida.append("Error: Faltan argumentos. Uso: actualizar_tarea <nombre_proyecto> <nombre_tarea> <nuevo_estado>")
            return
        
        nombre_proyecto = args[1]
        nombre_tarea = args[2]
        nuevo_estado = args[3]
        
        # Validamos que el nuevo estado sea uno de los estados válidos
        estados_validos = ["PENDIENTE", "EN_PROGRESO", "COMPLETADA"]
        if nuevo_estado.upper() not in estados_validos:
            salida.append(f"Error: Estado inválido. Estados válidos: {', '.join(estados_validos)}")
            return
        
        # Busca por nombre el id del proyecto
        id_proyecto = None
        for pid, proyecto in proyectos.items():
            if proyecto["Nombre"].lower() == nombre_proyecto.lower():
                id_proyecto = pid
                break
        
        if id_proyecto is None:# Si no encuentra el nombre del proyecto por ID te comunica que no existe
            salida.append(f"Error: El proyecto '{nombre_proyecto}' no existe.")
            return
        
        # Verificar que el proyecto tenga tareas
        if "Tareas" not in proyectos[id_proyecto] or not proyectos[id_proyecto]["Tareas"]:
            salida.append(f"Error: El proyecto '{nombre_proyecto}' no tiene tareas.")
            return
        
        # Buscar la tarea por nombre
        tarea_encontrada = None
        for tid, tarea in proyectos[id_proyecto]["Tareas"].items():
            if tarea["Nombre"].lower() == nombre_tarea.lower():
                tarea_encontrada = tarea
                break
        
        if tarea_encontrada is None:
            salida.append(f"Error: La tarea '{nombre_tarea}' no existe en el proyecto '{nombre_proyecto}'.")
            return
        
        # Actualizar el estado de la tarea
        tarea_encontrada["Estado"] = nuevo_estado.upper()
        
        manejoJson.guardar_proyectos(proyectos)
        salida.append(f'Estado de la tarea "{nombre_tarea}" actualizado a "{nuevo_estado.upper()}".')
        
    except IndexError:
        salida.append("Error: Faltan argumentos para actualizar la tarea.")
    except Exception as e:
        salida.append(f"Error inesperado: {str(e)}")