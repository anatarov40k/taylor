import math


def approximate_exp_with_pade_10(x):
    a0 = 1
    a1 = 1 / 2
    a2 = 9 / 76
    a3 = 1 / 57
    a4 = 7 / 3876
    a5 = 7 / 51680
    a6 = 7 / 930240
    a7 = 1 / 3255840
    a8 = 1 / 112869120
    a9 = 1 / 6094932480
    a10 = 1 / 670442572800

    result = (
            (a10*x**10 + a9*x**9 + a8*x**8 + a7*x**7 + a6*x**6 + a5*x**5 + a4*x**4 + a3*x**3 + a2*x**2 + a1*x + a0)
            /
            (a10*x**10 - a9*x**9 + a8*x**8 - a7*x**7 + a6*x**6 - a5*x**5 + a4*x**4 - a3*x**3 + a2*x**2 - a1*x + a0)
    )

    return result

x = 1.0

approx_value = approximate_exp_with_pade_10(x)
exact_value = math.exp(x)

print(f"Approximation e^{x}: {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
