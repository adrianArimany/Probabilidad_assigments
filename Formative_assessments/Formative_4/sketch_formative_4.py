
import scipy as sc
import sympy as sy
import numpy as np

x = sy.symbols('x', real=True)
f = 2*x

# Calculate the expectation (mean value) of the function f over the interval [0, 1]
expectation = sy.integrate(f * x, (x, 0, 1))

print(f"Expectation: {expectation}")

expectation_x2 = sy.integrate(x**2 * f, (x, 0, 1))

variance = expectation_x2 - expectation**2

print(f"Variance: {variance}")



# Define the symbol
t = sy.symbols('t')
T = sy.symbols('T')  # Capacity to solve for

# Define the PDF
g = 5 * (1 - t)**4

# Compute the cumulative probability integral from 0 to T
F_T = sy.integrate(g, (t, 0, T))

# Solve for T such that F_T = 0.99
result = sy.solve(F_T - 0.99 ,T)

# Print result
print(f"Capacity T: {sy.re(result[0])}")



# Calculate the expectation (mean value) of the function f over the interval [0, 1]
expectation = sy.integrate(f * x, (x, 0, 1))





# Define the piecewise function for f(x)
def pdf(x):
    return np.piecewise(
        x,
        [((10 <= x) & (x < 20)), #The first "box" in the PDF
         ((20 <= x) & (x < 30)),  # The middle box in the PDF
         ((30 <= x) & (x <= 40))], # THe thired box in the PDF
        [0.025, 0.05, 0.025] #The peaks of the probabilities in the PDF
    )

# Function to calculate probability by integrating the PDF over an interval
def probability(a, b):
    prob = 0
    if a < 20 and b > 10:
        start = max(a, 10)
        end = min(b, 20)
        prob += 0.025 * max(0, end - start)
    if a < 30 and b > 20:
        start = max(a, 20)
        end = min(b, 30)
        prob += 0.05 * max(0, end - start)
    if a <= 40 and b > 30:
        start = max(a, 30)
        end = min(b, 40)
        prob += 0.025 * max(0, end - start)

    return prob

# Compute the required probabilities
p_a = 1 - probability(10, 15)  # P(X > 15) = 1 - P(X ≤ 15) = 1 - P(10 < X ≤ 15)
p_b = probability(20, 35)      # P(20 ≤ X ≤ 35) = P(X ≤ 35) - P(X ≤ 20)
p_c = probability(10, 30)      # P(X < 30) 
p_d = probability(36, 40)      # P(X > 36) = 1 - P(X ≤ 36) = 1 - P(30 < X ≤ 36)

# Print the results
print(f"Problem A: P(X > 15) = {p_a:.3f}")
print(f"Problem B: P(20 ≤ X ≤ 35) = {p_b:.3f}")
print(f"Problem C: P(X < 30) = {p_c:.3f}")
print(f"Problem D: P(X > 36) = {p_d:.3f}")





