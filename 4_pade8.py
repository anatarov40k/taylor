import math


def approximate_exp_with_pade_8(x):
    a0 = 1
    a1 = 1 / 2
    a2 = 7 / 60
    a3 = 1 / 60
    a4 = 1 / 624
    a5 = 1 / 9360
    a6 = 1 / 205920
    a7 = 1 / 7207200
    a8 = 1 / 518918400

    result = (
            (a8*x**8 + a7*x**7 + a6*x**6 + a5*x**5 + a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0)
            /
            (a8*x**8 - a7*x**7 + a6*x**6 - a5*x**5 + a4*x**4 - a3*x**3 + a2*x**2 - a1*x + a0)
    )

    return result


x = 1.0

approx_value = approximate_exp_with_pade_8(x)
exact_value = math.exp(x)

print(f"Approximation e^{x}: {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
