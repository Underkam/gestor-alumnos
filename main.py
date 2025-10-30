# main.py
# Programa principal del Gestor de Alumnos
# ----------------------------------------
# Este módulo muestra el menú principal y coordina las acciones del programa.
# Importa las funciones de los módulos:
# - funciones_alumnos.py → gestión de alumnos (altas, búsquedas, listado)
# - estadisticas.py → cálculos de estadísticas del grupo

import os
from colorama import init, Fore
from funciones_alumnos import get_alumnos, mostrar_alumnos, anadir_alumno, buscar_alumno
from estadisticas import get_results
 

# Inicializa colorama (necessari per Windows)
init(autoreset=True)

alumnos = get_alumnos()

def show_menu() -> None:
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print(Fore.CYAN + "-" * 45)
    print(Fore.YELLOW + "************ MENÚ PRINCIPAL ************")
    print(Fore.GREEN + "1." + Fore.WHITE + " Ver lista de alumnos")
    print(Fore.GREEN + "2." + Fore.WHITE + " Añadir un nuevo alumno")
    print(Fore.GREEN + "3." + Fore.WHITE + " Buscar un alumno por nombre")
    print(Fore.GREEN + "4." + Fore.WHITE + " Mostrar estadísticas del grupo")
    print(Fore.RED   + "5." + Fore.WHITE + " Salir")
    print(Fore.CYAN + "-" * 45)


def get_option(mensaje, minimo=None, maximo=None):
    """
    Solicita al usuario una opción numérica y valida que esté dentro de un rango.
    """
    while True:
        try:
            valor = int(input(Fore.YELLOW + mensaje).strip())

            if minimo is not None and valor < minimo:
                print(Fore.RED + f"❌ Debes ingresar un número entre {minimo} y {maximo}.")
                continue

            if maximo is not None and valor > maximo:
                print(Fore.RED + f"❌ Debes ingresar un número entre {minimo} y {maximo}.")
                continue

            return valor

        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Introduce un número válido.")
        except (EOFError, KeyboardInterrupt):
            print(Fore.MAGENTA + "\n⚠️ Entrada interrumpida por el usuario.")
            raise


def main() -> None:
    """
    Controla el flujo principal del programa.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        # Mostrar menú
        show_menu()
        opcion = get_option('Elije una opción: ', 1, 5)

        match opcion:
            case 1:
                mostrar_alumnos(alumnos)
            case 2:
                anadir_alumno(alumnos)
            case 3:
                buscar_alumno(alumnos)
            case 4:
                get_results(alumnos)
            case 5:
                print(Fore.GREEN + "\n✅ Sistema cerrado. ¡Hasta pronto!")
                break
            case _:
                print(Fore.RED + "❌ Opción no válida. Elige un número del 1 al 5.")

        if opcion in {1, 2, 3, 4}:
            input(Fore.YELLOW + '\nPulsa Enter para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
