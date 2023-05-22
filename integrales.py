#para integral indefinida
from sympy import integrate
from sympy.abc import x

funcion1 = x ** 2 + 2 * x - 3
resultado1 = integrate(funcion1, x)
print("El resultado de la integral es:", resultado1)
