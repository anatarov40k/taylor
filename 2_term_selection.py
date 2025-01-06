import math

def approximate_exp_with_adaptive_taylor(x, allowed_error):
    result = 0
    term = 1
    k = 0

    while abs(term) > allowed_error:
        result += term
        k += 1
        term = (x**k) / math.factorial(k)

    return result, k

x = 1.0
allowed_error = 1e-8

approx_value, polynomial_order = approximate_exp_with_adaptive_taylor(x, allowed_error)
exact_value = math.exp(x)

print(f"Approximation e^{x} (used order {polynomial_order}): {approx_value}")
print(f"Exact value e^{x}: {exact_value}")
print(f"Error: {abs(approx_value - exact_value)}")
