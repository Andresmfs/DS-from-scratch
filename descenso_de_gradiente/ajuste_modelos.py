from typing import TypeVar, Iterator
from typing import List
import random
from est_cociente_diferencias import gradient_step
from vectores import vector_mean

Vector = List[float]

# Queremos ajustar con una recta una serie de puntos utilizando el gradiente
# Generamos esos puntos
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercep = theta
    predicted = slope * x + intercep
    error = predicted - y
    sq_error = error ** 2
    grad = [2 * error * x, 2 * error]
    return grad


theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

for epoch in range(5000):
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1
assert 4.9 < intercept < 5.1

###################
# Descenso del gradiente en minilotes

T = TypeVar('T')


def minibatches(dataset: List[T],
                batch_size=int,
                shuffle: bool = True) -> Iterator[List[T]]:
    """Genera minibatches del dataset de tamaño 'batch_size'"""
    batch_starts = [start for start in range(0, len(dataset), batch_size)]

    if shuffle:
        random.shuffle(batch_starts)
    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]

# Resolvemos el problema anterior utilizando minibatches en lugar del total de datos


theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

for epoch in range(1000):
    for batch in minibatches(inputs, batch_size=20):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1
assert 4.9 < intercept < 5.1


# Descenso del gradiente estocástico
for epoch in range(100):
    for x, y in inputs:
        grad = linear_gradient(x, y, theta)
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1
assert 4.9 < intercept < 5.1
