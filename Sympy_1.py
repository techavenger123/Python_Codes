import sympy as sp

n, z = sp.symbols('n z')
x_n = 3**n * sp.Heaviside(n)  # Heaviside function u[n]
Z_transform = sp.Sum(x_n * z**(-n), (n, 0, sp.oo)).doit()
print("Z-transform of x[n] = 3^n u[n]:")
sp.pprint(Z_transform)
