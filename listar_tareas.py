def listar_tareas(args, proyectos, salida):
    nombre_proyecto = args[1]
    
    #  Verificar si se especifica un filtro de estado
    estado_filtro = None
    if len(args) > 2:
        estado_filtro = args[2].upper()

    proyecto_encontrado = None
    for proyecto in proyectos.values():
        if proyecto["Nombre"].lower() == nombre_proyecto.lower():
            proyecto_encontrado = proyecto
            break

    if not proyecto_encontrado:
        salida.append(f"No se encontró el proyecto '{nombre_proyecto}'.")
        return

    # Modificar título según filtro
    if estado_filtro:
        salida.append(f"=== Tareas del proyecto '{nombre_proyecto}' en estado '{estado_filtro}' ===")
    else:
        salida.append(f"=== Tareas del proyecto '{nombre_proyecto}' ===")

    tareas = proyecto_encontrado.get("Tareas", {})
    if not tareas:
        salida.append("Este proyecto no tiene tareas.")
        return

    # Filtrar tareas por estado si se especifica
    tareas_mostrar = {}
    for tid, tarea in tareas.items():
        if not estado_filtro or tarea['Estado'].upper() == estado_filtro:
            tareas_mostrar[tid] = tarea
    
    if not tareas_mostrar:
        salida.append(f"No hay tareas en estado '{estado_filtro}'.") 
        return

    for tid, tarea in tareas_mostrar.items():
        salida.append(f"- [{tid}] {tarea['Nombre']} - Responsable: {tarea['Responsable']} - Estado: {tarea['Estado']}")