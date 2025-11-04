import math

def f(x):
    return x**2 - 1 - math.exp(1 - x**2)

a = -2
b = 0
error = 1

while error > 1e-5:
    c = (a + b)/2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    error = abs(b - a)

print("Raíz aproximada en [-2,0]:", (a+b)/2)
