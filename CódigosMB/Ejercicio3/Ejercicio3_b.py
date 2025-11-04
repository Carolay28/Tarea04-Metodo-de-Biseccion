import math

def f(x):
    return x - math.tan(x)

a = 0
b = math.pi/2 - 0.01
error = 1

while error > 1e-5:
    c = (a + b)/2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    error = abs(b - a)

print("Primer valor positivo de x aproximado:", (a+b)/2)
