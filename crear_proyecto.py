import main

#a modo de ejemplo tenemos un proyecto ya ingresado.
proyectos = {
    1 : {
        "Nombre": "Proyecto final",
        "Descripcion": "Obligatorio final de clase",
        "FechaLimite": 1003882,
        "Tareas": {
            1 : {
                "Nombre": "Realizar layout",
                "Descripcion": 27,
                "Responsable": "Agustin",
                "FechaLimite": 1003882,
                "Estado": ""
            }
        }
    }
}

def crear_proyecto(args, salida): #Toma argumentos y los valida generando un dato "salida" que usaremos despues para el output del programa por txt
    try:
        id = args[1]  #Clave para la lista de proyectos
        nombre = args[2] #Nombre del proyecto
        descripcion = args[3] #Descripcion
        fecha_limite = int(args[4])  # formato: AAAAMMDD

        if id in proyectos:
            salida.append(f"Ya existe un proyecto con clave '{id}'") #En caso de que la id ya este ingresada imprime en el txt
        else:
            proyectos[id] = {
                "Nombre": nombre,
                "Descripcion": descripcion,
                "FechaLimite": fecha_limite,
                "Tareas": {}
            }
            salida.append(f"Proyecto '{nombre}' creado con éxito.") #En caso de que los datos dados sean correctos se expresa el exito de la ejecucion 
    except IndexError:
        salida.append("Error: Faltan argumentos. Uso: crear_proyecto clave nombre descripcion fechaLimite") #En caso de que los datos dados no sean la cantidad correcta
    except ValueError:
        salida.append("Error: Fecha límite debe ser un número entero (formato AAAAMMDD)") #En caso de que los datos dados no sean la cantidad correcta



