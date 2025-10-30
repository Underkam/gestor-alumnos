# main.py
# Programa principal del Gestor de Alumnos
# ----------------------------------------
# Este módulo muestra el menú principal y coordina las acciones del programa.
# Importa las funciones de los módulos:
# - funciones_alumnos.py → gestión de alumnos (altas, búsquedas, listado)
# - estadisticas.py → cálculos de estadísticas del grupo

import os


def show_menu() -> None:
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("-" * 40)
    print("************ MENÚ PRINCIPAL ************")
    print("1. Ver lista de alumnos")
    print("2. Añadir un nuevo alumno")
    print("3. Buscar un alumno por nombre")
    print("4. Mostrar estadísticas del grupo")
    print("5. Salir")
    print("-" * 40)


def get_option(mensaje, minimo=None, maximo=None):
    """
    Solicita al usuario una opción numérica y valida que esté dentro de un rango.
    """
    while True:
        try:
            valor = int(input(mensaje).strip())

            if minimo is not None and valor < minimo:
                print(f"❌ Debes ingresar un número {minimo} - {maximo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"❌ Debes ingresar un número entre {minimo} - {maximo}.")
                continue

            return valor

        except ValueError:
            print("❌ Entrada inválida. Introduce un número válido.")
        except (EOFError, KeyboardInterrupt):
            print("\n⚠️ Entrada interrumpida por el usuario.")
            raise


def main() -> None:
    """
    Controla el flujo principal del programa.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        # Muestro menu opciones.
        show_menu()
        # Selecciono opción del usuario.
        opcion = get_option('Elije una opción: ', 1, 5)

        match opcion:
            case 1:
                print(1)
            case 2:
                print(2)
            case 3:
                print(3)
            case 4:
                print(4)
            case 5:
                print("\n✅ Sistema cerrado. ¡Hasta pronto!")
                break
            case _:
                print("❌ Opción no válida. Elige un número del 1 al 5.")

        if opcion in {1, 2, 3, 4}:
            input('\nPulsa Enter para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
