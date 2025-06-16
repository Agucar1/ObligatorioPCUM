from datetime import datetime
import manejoJson

def crear_tarea(args, proyectos, salida): # creamos un proyecto apartir de 6 parametros dados por lina de comando
   
    try:
        nombre_proyecto = args[1]
        nombre = args[2]
        descripcion = args[3]
        responsable = args[4]
        fecha_str = args[5]
        estado = args[6]

        try: # Validamos la fecha
            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            salida.append("Error: Fecha límite inválida. Usa formato AAAA-MM-DD con una fecha real.")
            return
        
        id_proyecto = None  
        for pid, proyecto in proyectos.items(): # Busca por nombre el ID del proyecto
            if proyecto["Nombre"].lower() == nombre_proyecto.lower():
                id_proyecto = pid
                break

        if id_proyecto is None: # Si no encuentra el nombre del proyecto por ID te comunica que no existe
            salida.append(f"Error: El proyecto '{nombre_proyecto}' no existe.")
            return
        
        try: 
           fecha_str_proyecto = proyectos[id_proyecto]['FechaLimite']
           fecha_limite_proyecto = datetime.strptime(fecha_str_proyecto, "%Y-%m-%d")
           if fecha_obj > fecha_limite_proyecto:
             salida.append("Error: La fecha de la tarea no puede ser posterior a la fecha límite del proyecto.")
             return
        except (KeyError, ValueError):
           salida.append("Error: Fecha del proyecto inválida o no encontrada.")
           return

        tareas = proyectos[id_proyecto]["Tareas"] # Generamos usa ruta mas corta para las tareas del proyecto

        for tarea in tareas.values(): # Validamos el nombre de la tarea
            if tarea["Nombre"].lower() == nombre.lower():
                salida.append(f"Ya existe una tarea con el nombre '{nombre}' en el proyecto '{nombre_proyecto}'")
                return
            
        if estado not in ["EN_PROGRESO", "COMPLETADA", "PENDIENTE"]:
         salida.append("Error: el estado debe ser EN_PROGRESO, COMPLETADA o PENDIENTE")
         return


        if tareas: # Generamos una nueva id para la tarea
            nuevo_id = str(max(int(tid) for tid in tareas.keys()) + 1)
        else:
            nuevo_id = "1"

        tareas[nuevo_id] = { # Parseamos la tarea
            "Nombre": nombre,
            "Descripcion": descripcion,
            "Responsable": responsable,
            "FechaLimite": fecha_str,
            "Estado": estado
        }

        manejoJson.guardar_proyectos(proyectos)
        salida.append(f"Tarea '{nombre}' creada con éxito en el proyecto '{nombre_proyecto}'.")

    except IndexError:
        salida.append("Error: Faltan argumentos. Uso: crear_tarea nombreProyecto nombre descripcion responsable fechaLimite estado")
