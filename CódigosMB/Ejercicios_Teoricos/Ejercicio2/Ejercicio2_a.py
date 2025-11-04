import math

def f(x):
    return math.sin(math.pi * x)

a = -0.5
b = 2.0  
tolerancia = 0.00001

while (b - a) > tolerancia:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("La raíz aproximada es:", c)