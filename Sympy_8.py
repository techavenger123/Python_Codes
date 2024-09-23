import sympy as sp

n, z, omega = sp.symbols('n z omega')
x_n = sp.cos(omega * n) * sp.Heaviside(n)  # Heaviside function u[n]
Z_transform = sp.Sum(x_n * z**(-n), (n, 0, sp.oo)).doit()
Z_transform_simplified = sp.simplify(Z_transform)
print("Z-transform of x[n] = cos(ωn) u[n]:")
sp.pprint(Z_transform_simplified)
