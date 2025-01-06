import math

def approximate_exp_with_chebyshev_interpolation_at_x_1(x,
nodes_number):
  # chebyshev nodes for interpolation
  x_nodes = [math.cos((2 * k + 1) / (2 * nodes_number) * math.pi) for k in range(nodes_number)]
  
  y_nodes = [math.exp(x) for x in x_nodes]

  # lagrange interpolation polynomial
  nodes_number = len(x_nodes)
  y_interp = 0
  for i in range(nodes_number):
    li = 1
    for j in range(nodes_number):
      if i != j:
        li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
    y_interp += li * y_nodes[i]
    
  return y_interp

x = 1.0
nodes_number = 10
approx_value = approximate_exp_with_chebyshev_interpolation_at_x_1(x, nodes_number)
exact_value = math.exp(1)

print(f&quot;Approximation e^{x} ({nodes_number} nodes): {approx_value}&quot;)
print(f&quot;Exact value e^{x}: {exact_value}&quot;)
print(f&quot;Error: {abs(approx_value - exact_value)}&quot;)
