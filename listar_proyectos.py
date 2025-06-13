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

def listar_proyectos(args):
    salida = [];

    if args[0].lower() == "listar_proyectos": # si el primer parametro ingresado por consola es "listar_proyectos" procede a llamar a la funcion de creacion de proyectos
            salida.append("=== Proyectos ===")
        for id, proyecto in proyectos.items(): # por cada velor dentro de proyectos, ingresa datos en "salida"  
            salida.append(f"Proyecto: {id}")
            salida.append(f"  Nombre: {proyecto['Nombre']}")
            salida.append(f"  Descripción: {proyecto['Descripcion']}")
            salida.append(f"  Fecha Límite: {proyecto['FechaLimite']}")
            salida.append("  Tareas:")
            for tid, tarea in proyecto["Tareas"].items():
                salida.append(f"    - {tid}: {tarea['Nombre']} ({tarea['Responsable']})")