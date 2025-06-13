def listar_tareas(args, proyectos, salida):

    nombre_proyecto = args[1]

    proyecto_encontrado = None
    for proyecto in proyectos.values():
        if proyecto["Nombre"].lower() == nombre_proyecto.lower():
            proyecto_encontrado = proyecto
            break

    if not proyecto_encontrado:
        salida.append(f"No se encontró el proyecto '{nombre_proyecto}'.")
        return

    salida.append(f"=== Tareas del proyecto '{nombre_proyecto}' ===")

    tareas = proyecto_encontrado.get("Tareas", {})
    if not tareas:
        salida.append("Este proyecto no tiene tareas.")
        return

    for tid, tarea in tareas.items():
        salida.append(f"- [{tid}] {tarea['Nombre']} - Responsable: {tarea['Responsable']} - Estado: {tarea['Estado']}")