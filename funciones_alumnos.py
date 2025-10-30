alumnos = None

def get_alumnos():
    global alumnos
    if not alumnos:
        alumnos = [
            {"nombre": "Ana", "edad": 20, "nota": 8.5},
            {"nombre": "Luis", "edad": 22, "nota": 6.9}
        ]

    return alumnos

def anadir_alumno(alumnos):
    alumno_agregar = input('Ingrese el nombre del alumno: ').lower()
    edad_agregar = int(input('Ingrese la edad del alumno: '))
    nota_agregar = float(input('Ingrese la nota a agregar: '))
    
    set_de_datos = {'nombre': alumno_agregar,'edad': edad_agregar, 'nota': nota_agregar}
    
    alumnos.append(set_de_datos)
    
    print(f'Alumno agregado correctamente {set_de_datos}')


def buscar_alumno(alumnos):
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")
    encontrado = False
    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre_buscar.lower():
            print(f"Alumno encontrado:")
            print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Nota: {alumno['nota']}")
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado.")

def mostrar_alumnos(alumnos):
    print("\nListado de alumnos:")
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Nota: {alumno['nota']}")
