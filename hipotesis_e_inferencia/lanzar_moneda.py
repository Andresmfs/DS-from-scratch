# Hipótesis e inferencia

from typing import List
import random
from typing import Tuple
import math
from distribuciones_prob import normal_cdf
from distribuciones_prob import inverse_normal_cdf


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Devuelve mu y sigma correspondientes al Binomial(n, p)"""
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    return mu, sigma


normal_probability_below = normal_cdf


def normal_probability_above(lo: float,
                             mu: float,
                             sigma: float) -> float:
    """Devuelve la probabilidad de que N(mu, sigma) esté por encima de cierto valor"""
    return (1 - normal_cdf(lo, mu, sigma))


def normal_probability_between(lo: float,
                               hi: float,
                               mu: float,
                               sigma: float) -> float:
    """Devuelve la probabilidad de que N(mu, sigma) se encuentre en el intervalo (lo, hi)"""
    return (normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma))


def normal_probability_outside(lo: float,
                               hi: float,
                               mu: float,
                               sigma: float) -> float:
    """Devuelve la probabilidad de que N(mu, sigma) se encuentre fuera del intervalo (lo, hi)"""
    return (1 - normal_probability_between(lo, hi, mu, sigma))


def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Devuelve el valor de z para el cual P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Devuelve el valor de z para el cual P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """Devuelve el intervalo simétrico (centrado en mu) que contiene la probabilidad indicada"""
    p_sides = (1 - probability) / 2
    upper_bound = normal_lower_bound(p_sides, mu, sigma)
    lower_bound = normal_upper_bound(p_sides, mu, sigma)
    return lower_bound, upper_bound


# Exploraremos la hipótesis de que el lanzamiento de una moneda de un probabilidad de 0,5 de que salga cara
# Rechazaremos la prueba si hay un error mayor que el 5%.
# Veamos en qué intervalo se concentra el 95% de los resultados
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print(mu_0, sigma_0)

lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print(lower_bound, upper_bound)

# ¿Qué pasaría si p = 0,55?¿Seguirá siendo válido el intervalo (lo, hi)?
# De ser así, esto sería un error tipo 2, pues no rechazaríamos nuestra hipótesis inicial
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
print(mu_1, sigma_1)

# 0,11 es la probabilidad de que estuviera en el intervalo anterior con la nueva probabilidad
type_2_probability = normal_probability_between(
    lower_bound, upper_bound, mu_1, sigma_1)
# Es la llamada potencia de la prueba, su valor es de 0,89
power = 1 - type_2_probability
print(type_2_probability, power)
# Esta prueba nos sirve para verificar si los resultados salen "fuera" de los esperados por una moneda justa
# No tiene en cuenta si se sale de lo esperado por estar inclinado a la cara o la cruz

# La prueba es más fiable si inspeccionamos si se desvía hacia una cara en concreto, por ejemplo cara
# 526 es valor por debajo del cual hay un 95% de posibilidades de obtener nuestro resultado
hi = normal_upper_bound(0.95, mu_0, sigma_0)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
# 0,94 es el poder de esta pueba (más potente que la prueba anterior)
power = 1 - type_2_probability


######################
# Valores p
# Para verificar la hipótesis
# Calculamos la probabilidad de ver un valor al menos tan extremo como el que hemos observado

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    Cómo de probable es ver un valor al menos tan extremo como x (en ambas direcciones) 
    si nuestros valores se encuentran en N(mu, sigma)
    """
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)


# Vi viéramos 530, ¿Cómo de probable sería para una "moneda justa"?
# Utilizamos 529.5, porque asumimos en 530 un error y conviene incorporar esa parte en nuestro resultado
extr_p_value = two_sided_p_value(529.5, mu_0, sigma_0)
print(extr_p_value)
# 0,062 es mayor que nuestra significancia del 5%, por tanto a priori no rechazamos la hipótesis

# Haremos una simulación para testear

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
    if num_heads <= 469 or num_heads >= 531:
        extreme_value_count += 1

# assert 59 < extreme_value_count < 65, f"{extreme_value_count}"

# Para la prueba de una sola cara en lugar de two_sided_p_value, utilizaríamos: normal_probability_above o normal probability_below

####################
# Intervalos de confianza
# Supongamos que en una prueba de las dos monedas obtenemos 525 caras de 1000 lanzamientos
# ¿Podemos descartar la posibilidad de que sea una "moneda justa" (con p = 0,5)?

p_hat = 530 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

low_p, hi_p = normal_two_sided_bounds(0.95, mu, sigma)
# Esta prueba debe pasarla en el 95% de las veces
assert low_p < 0.5 < hi_p, f"No es una moneda justa, low_p = {low_p} y hi_p = {hi_p}"

# p-hacking


def run_experiment() -> List[bool]:
    """Lanza una moneda justa 1000 veces, True = cara, False = cruz"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment: List[bool]) -> bool:
    """Usando el 5% de nivel de significancia"""
    num_heads = len([flip for flip in experiment if flip])
    # El intervalo (469, 531) es donde vimos que se concentraban en 95% de los reultados
    # Contabilizamos el número de resultados favorables que quedan fuera de ese 95%
    return num_heads < 469 or num_heads > 531


random.seed(78)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len(
    [experiment for experiment in experiments if reject_fairness(experiment)])

print(num_rejections)
