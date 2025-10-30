"""
estadisticas.py
---------------------
Contiene funciones para realizar operaciones estadisticas:

- Calcular media.
- Calcular número mayor.
- Calcular número menor.
- Mostar estadisticas.
"""


def media_alumnos(alumnos: list[dict]) -> float:
    """
    Calcula la media aritmética de los valores de una 'clave' (ej. 'nota', 'edad')
    en una lista de diccionarios de alumnos.

    Args:
        alumnos (list[dict]): Lista de diccionarios de alumnos.

    Returns:
        float: El valor de la media aritmética.

    """
    notas = [alumno['nota'] for alumno in alumnos]

    media = sum(notas) / len(notas)
    return media


def is_mayor_alumnos(alumnos: list[dict]) -> float:
    """
    Devuelve el valor más alto de una 'clave' (ej. 'nota', 'edad')
    en una lista de diccionarios de alumnos.

    Args:
        alumnos (list[dict]): Lista de diccionarios de alumnos.

    Returns:
        float: El valor más grande encontrado.
    """
    notas = [alumno['nota'] for alumno in alumnos]

    return max(notas)

def is_menor_alumnos(alumnos: list[dict]) -> float:
    """
    Devuelve el valor más bajo de una 'clave' (ej. 'nota', 'edad')
    en una lista de diccionarios de alumnos.

    Args:
        alumnos (list[dict]): Lista de diccionarios de alumnos.
        clave (str): La clave del diccionario cuyo valor se usará para la comparación.

    Returns:
        float: El valor más pequeño encontrado.
    """
    notas = [alumno['nota'] for alumno in alumnos]

    return min(notas)


def get_results(alumnos):

    media = media_alumnos(alumnos)
    nota_max = is_mayor_alumnos(alumnos)
    nota_min = is_menor_alumnos(alumnos)

    print("--- Resultados ---")
    print(f"**Media de notas:** {media:.2f}")
    print(f"**Nota Máxima:** {nota_max}")
    print(f"**Nota Mínima:** {nota_min}")
    print("-" * 35)
