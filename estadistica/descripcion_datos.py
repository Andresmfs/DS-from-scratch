import math
from collections import Counter
import matplotlib.pyplot as plt
# import random
from typing import List
from vectores import sum_of_squares
Vector = List[float]


# # Creamos nuestros datos de forma aleatoria
# random.seed(1)
# num_friends = [random.choice(range(101)) for _ in range(500)]
num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Creamos el histograma
histogram = Counter(num_friends)

xs = range(101)
ys = [histogram[x] for x in xs]
plt.bar(xs, ys, edgecolor=(0, 0, 0))
plt.axis([0, 101, 0, max(ys) + 3])

plt.title("Histograma de recuento de amigos")
plt.ylabel("Nº de gente")
plt.xlabel("Nº de amigos")
# plt.show()
# plt.savefig('recuento.jpg')
plt.gca().clear()
# Número de puntos de datos
num_points = len(num_friends)

# Valores mayor y menor
largest = max(num_friends)
smallest = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_largest_value = sorted_values[-2]
print(largest, smallest_value, second_largest_value)

# Tendencias centrales


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


assert mean([1, 2, 3]) == 2
print(mean(num_friends))


def _median_odd(xs: List[float]) -> float:
    """Calcula la mediana de un número impar de datos"""
    return sorted(xs)[len(xs)//2]


def _median_even(xs: List[float]) -> float:
    """Calcula la mediana de un número par de datos"""
    x_sort = sorted(xs)
    midpoint = len(xs)//2
    return (x_sort[midpoint] + x_sort[midpoint - 1])/2


def median(xs: List[float]) -> float:
    if len(xs) % 2 == 0:
        return _median_even(xs)
    else:
        return _median_odd(xs)


assert median([1, 10, 9, 5, 2]) == 5
assert median([1, 9, 2, 4]) == 3

print(median(num_friends))


def quantile(xs: List[float], s: float) -> float:
    """Devuelve el valor del s-percentil de xs"""
    p_index = int(s * len(xs))
    return sorted(xs)[p_index]


assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13


def mode(xs: List[float]) -> float:
    """Calcula la moda de un conjunto de datos"""
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, counts in counts.items() if counts == max_count]


assert set(mode(num_friends)) == {1, 6}

# Medidas de dispersión


def data_range(xs: List[float]) -> float:
    """Calcula el rango"""
    return max(xs) - min(xs)


assert data_range([3, 5, 10]) == 7


def de_mean(xs: List[float]) -> float:
    return [x_i-mean(xs) for x_i in xs]


def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations)/(n - 1)


assert 81.54 < variance(num_friends) < 81.55


def standard_deviation(xs: List[float]) -> float:
    """El cuadrado de la varianza"""
    return math.sqrt(variance(xs))


assert 9.02 < standard_deviation(num_friends) < 9.04


def interquartile_range(xs: List[float]) -> float:
    """Devuelve la diferencia entre los percentiles 75 y 25"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


assert interquartile_range(num_friends) == 6
