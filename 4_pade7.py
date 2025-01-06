import math


def approximate_exp_with_pade_7(x):
    a0 = 1
    a1 = 1 / 2
    a2 = 3 / 26
    a3 = 5 / 312
    a4 = 5 / 3432
    a5 = 1 / 11440
    a6 = 1 / 308880
    a7 = 1 / 17297280

    result = (
            (a7*x**7 + a6*x**6 + a5*x**5 + a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0)
            /
            (-a7*x**7 + a6*x**6 - a5*x**5 + a4*x**4 - a3*x**3 + a2*x**2 - a1*x + a0)
    )

    return result


x = 1.0

approx_value = approximate_exp_with_pade_7(x)
exact_value = math.exp(x)

print(f"Approximation e^{x}: {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
