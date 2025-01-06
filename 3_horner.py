import math


def approximate_exp_with_horner(x, polynomial_order):
    result = 1

    for k in range(polynomial_order, 0, -1):
        result = 1 + x * result / k

    return result


x = 1.0
polynomial_order = 10

approx_value = approximate_exp_with_horner(x, polynomial_order)
exact_value = math.exp(x)

print(f"Approximation e^{x} (order {polynomial_order}): {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
