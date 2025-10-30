alumnos = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 6.9}
]

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
