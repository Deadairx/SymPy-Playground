from sympy import *

Va, Vp, Vpx, D, t = symbols('Va Vp Vpx D t')

solution = solve([
    Vp - Va * Vpx,
    Va * t + Vp * t - D
], (Va, Vp))

print(solution)
