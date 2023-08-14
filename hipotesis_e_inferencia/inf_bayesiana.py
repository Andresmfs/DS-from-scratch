import math
import matplotlib.pyplot as plt


def B(alpha: float, beta: float) -> float:
    """Constante de normalización para que la probabilidad total sea 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)


xs = [(x_i + 0.01) / 100 for x_i in range(99)]

plt.plot(xs, [beta_pdf(x_i, alpha=1, beta=1)
         for x_i in xs], '-', label="Beta(1, 1)")
plt.plot(xs, [beta_pdf(x_i, alpha=5, beta=5)
         for x_i in xs], '.', label="Beta(5, 5)")
plt.plot(xs, [beta_pdf(x_i, alpha=3, beta=7)
         for x_i in xs], '-.', label="Beta(3, 7)")
plt.plot(xs, [beta_pdf(x_i, alpha=7, beta=3)
         for x_i in xs], '--', label="Beta(7, 3)")
plt.plot(xs, [beta_pdf(x_i, alpha=10, beta=10)
         for x_i in xs], ':', label="Beta(10, 10)")

plt.title("Ejemplos distribuciones beta")
plt.legend(loc=1)
plt.show()
