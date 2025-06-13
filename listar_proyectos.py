def listar_proyectos(proyectos, salida):
    salida = []

    if not proyectos: # Validamos que existan proyectos para listar
        salida.append("No hay proyectos guardados.")
        return salida

    salida.append("=== Proyectos ===") # Guaradamos todos los datos del proyecto en la lista salida
    for id, proyecto in proyectos.items():
        salida.append(f"Proyecto: {id}")
        salida.append(f"  Nombre: {proyecto['Nombre']}")
        salida.append(f"  Descripción: {proyecto['Descripcion']}")
        salida.append(f"  Fecha Límite: {proyecto['FechaLimite']}")
        salida.append("  Tareas:")
        for tid, tarea in proyecto["Tareas"].items():
            salida.append(f"    - {tid}: {tarea['Nombre']} ({tarea['Responsable']})")
    
    return salida #retormanos la lista para incluir en nuestro output txt