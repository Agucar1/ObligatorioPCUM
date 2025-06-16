
Funcionalidades del gestor de proyectos.

CREACION DE PROYECTO:

python main.py crear_proyecto "Proyecto1" "Proyecto de ejemplo para
gestionar tareas" "2025-06-30"

LISTADO DE PROYECTOS:

python main.py listar_proyectos

CREAR TAREA:

python main.py crear_tarea  "ChatGPT 4.0" "Prueba 2" "Validacion de fecha" "Agustin" "2025-02-09"  "COMPLETADA"

ACTUALIZAR TAREA:

python main.py actualizar_tarea "Obligatorio" "Funcionalidad crear proyecto" "PENDIENTE"

LISTAR TAREAS:

python main.py listar_tareas "Obligatorio"

LISTAR TAREAS CON FILTRO DE ESTADO:

python main.py listar_tareas "CHATGPT 4.0" "PENDIENTE"

---- VALIDACIONES ----

No se pueden ingresar proyectos con el mismo nombre, ni tareas con el mismo nombre 

No se pueden ingresar tareas en un proyecto inexistente

La fecha limite ingresada para una tarea no puede ser posterior a la fecha limite del proyecto

Github:
https://github.com/Agucar1/ObligatorioPCUM



