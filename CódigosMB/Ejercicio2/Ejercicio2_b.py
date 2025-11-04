import math

def f(x):
    return x - 2*math.sin(x)

a = 0
b = 2
error = 1

while error > 1e-5:
    c = (a + b)/2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    error = abs(b - a)

print("Primer valor positivo de x aproximado:", (a+b)/2)
