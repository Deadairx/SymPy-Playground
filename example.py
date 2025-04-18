from sympy import symbols, solve, diff, integrate

# Define symbolic variables
x = symbols('x')

# Example 1: Basic arithmetic
expr = x**2 + 2*x + 1
print("Expression:", expr)

# Example 2: Differentiation
derivative = diff(expr, x)
print("Derivative:", derivative)

# Example 3: Integration
integral = integrate(expr, x)
print("Integral:", integral)

# Example 4: Solving equations
equation = x**2 - 4
solution = solve(equation, x)
print("Solution to x^2 - 4 = 0:", solution) 