import math


def approximate_exp_with_pade_5(x):
    a0 = 1
    a1 = 1 / 2
    a2 = 1 / 9
    a3 = 1 / 72
    a4 = 1 / 1008
    a5 = 1 / 30240

    result = (
            (a5*x**5 + a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0)
            /
            (-a5*x**5 + a4*x**4 - a3*x**3 + a2*x**2 - a1*x + a0)
    )

    return result


x = 1.0

approx_value = approximate_exp_with_pade_5(x)
exact_value = math.exp(x)

print(f"Approximation e^{x}: {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
