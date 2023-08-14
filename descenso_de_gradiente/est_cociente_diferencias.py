from vectores import distance, add, scalar_multiply
import random
import matplotlib.pyplot as plt
from typing import List
from typing import Callable

Vector = List[float]


def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h


def square(x: float) -> float:
    return x * x


def sq_derivative(x: float) -> float:
    return 2 * x


xs = range(-10, 11)
actuals = [sq_derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

plt.plot(xs, actuals, 'rx', label="Valor real")
plt.plot(xs, estimates, 'b*', label="Valor estimado")
plt.legend(loc=9)
# plt.show()


def partial_difference_quotient(f: Callable[[Vector], float], v: Vector, i: int, h: float) -> float:
    """Calcula el cociente de diferencias parcial del iésimo elemento de f en v"""
    w = [v_j + (h if i == j else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f: Callable[[Vector], float], v: Vector, h: float = 0.0001) -> Vector:
    return [partial_difference_quotient(f, v, i, h) for i in range(len(v))]
# Esta función consume mucha capacidad computacional.
# Si es posible se calculará el gradiente a mano de manera analítica.


# Ejemplo de minimización usando el gradiente sobre la función sum_of_squares(v)


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    assert len(v) == len(gradient), "vectors must be same length"
    step = scalar_multiply(step_size, gradient)
    return add(step, v)


def sum_of_square_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]


v = [random.uniform(-10, 10) for i in range(3)]
for epoch in range(1000):
    grad = sum_of_square_gradient(v)
    v = gradient_step(v, grad, -0.01)
    # print(epoch, v)

assert distance(v, [0, 0, 0]) < 0.001
