# Crearemos funciones para realizar las operaciones básicas con vectores
# suma de dos vectores, de varios vectores, productor de un vector y un escalar, producto escalar, módulo...

# Definimos un vector como una lista de flotantes
import math
from typing import List
Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Esta función permite hacer una suma entre dos vectores"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """Esta función permite hacer una resta entre dos vectores"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 2, 3], [4, 5, 3]) == [1, -3, 0]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Suma varios vectores"""
    # comprueba que los vectores no estén vacíos
    assert vectors, "no vectors provided"

    num_elements = len(vectors[0])
    assert all(
        len(v) == num_elements for v in vectors), "all vectors must be same length"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Esta función multiplica un escalar por un vector"""

    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Calcula la media por componentes de una lista de vectores"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2], [3, 4]) == 11


def sum_of_squares(v: Vector) -> float:
    """Calcula la suma de los elementos de un vector al cuadrado"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 1 + 4 + 9


def magnitude(v: Vector) -> float:
    """Calcula el módulo de un vector"""
    return math.sqrt(sum_of_squares(v))


assert magnitude([4, 3]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    """Calcula el cuadrado de la distancia entre dos vectores"""
    s = subtract(v, w)
    return sum_of_squares(s)


assert squared_distance([2, 4], [1, 2]) == 5


def distance(v: Vector, w: Vector) -> float:
    """Calcula la distancia entre dos vectores"""
    return math.sqrt(squared_distance(v, w))


a = [1, 4, 0, 5]
b = [3, 6, 9, 1]

print(add(a, b))
print(subtract(a, b))
print(scalar_multiply(3, a))
