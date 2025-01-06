import math


def approximate_exp_with_naive_taylor(x, polynomial_order):
    result = 0
    for n in range(polynomial_order + 1):
        term = (x ** n) / math.factorial(n)
        result += term
    return result


x = 1.0
polynomial_order = 10

approx_value = approximate_exp_with_naive_taylor(x, polynomial_order)
exact_value = math.exp(x)

print(f"Approximation e^{x} (order {polynomial_order}): {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
