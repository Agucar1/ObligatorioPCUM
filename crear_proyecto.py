import manejoJson

def crear_proyecto(args, proyectos, salida): # creamos un proyecto apartir de 3 parametros dados por lina de comando
    try:
        nombre = args[1] 
        descripcion = args[2]
        fecha_limite = int(args[3])

        for p in proyectos.values(): #recorremos proyectos para checkear que el nombre del mismo no exista
            if p["Nombre"].lower() == nombre.lower():
                salida.append(f"Ya existe un proyecto con el nombre '{nombre}'")
                return

        if proyectos: #generamos un id ingremental para cada proyecto
            nuevo_id = str(max(int(pid) for pid in proyectos.keys()) + 1)
        else:
            nuevo_id = "1"

        proyectos[nuevo_id] = {  #Parseamos los valores dados por parametro
            "Nombre": nombre,
            "Descripcion": descripcion,
            "FechaLimite": fecha_limite,
            "Tareas": {}
        }

        manejoJson.guardar_proyectos(proyectos) # Con la funcion del gestor de datos JSON guardamos el proyecto.
        salida.append(f"Proyecto '{nombre}' creado con éxito con ID {nuevo_id}.")

    except IndexError: # Gestionamos errores de falta de parametros y error de fecha.
        salida.append("Error: Faltan argumentos. Uso: crear_proyecto nombre descripcion fechaLimite")
    except ValueError:
        salida.append("Error: Fecha límite debe ser un número entero (formato AAAAMMDD)")


