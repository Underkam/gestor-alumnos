# main.py
# Programa principal del Gestor de Alumnos
# ----------------------------------------
# Este módulo muestra el menú principal y coordina las acciones del programa.
# Importa las funciones de los módulos:
# - funciones_alumnos.py → gestión de alumnos (altas, búsquedas, listado)
# - estadisticas.py → cálculos de estadísticas del grupo

from funciones_alumnos import (
    ver_lista_alumnos,
    agregar_alumno,
    buscar_alumno_por_nombre
)

from estadisticas import mostrar_estadisticas


def mostrar_menu():
    """Muestra el menú principal por pantalla."""
    print("\n=== GESTOR DE ALUMNOS ===")
    print("1. Ver lista de alumnos")
    print("2. Añadir un nuevo alumno")
    print("3. Buscar un alumno por nombre")
    print("4. Mostrar estadísticas del grupo")
    print("5. Salir")


def main():
    """Función principal del programa."""
    # Lista inicial de alumnos en memoria
    alumnos = [
        {"nombre": "Ana", "edad": 20, "nota": 8.5},
        {"nombre": "Luis", "edad": 22, "nota": 6.9}
    ]

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            ver_lista_alumnos(alumnos)
        elif opcion == "2":
            agregar_alumno(alumnos)
        elif opcion == "3":
            buscar_alumno_por_nombre(alumnos)
        elif opcion == "4":
            mostrar_estadisticas(alumnos)
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
