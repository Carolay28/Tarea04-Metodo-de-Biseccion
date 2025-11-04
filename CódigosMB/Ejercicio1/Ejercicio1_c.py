def f(x):
    return x**3 - 7*x**2 + 14*x - 6

a = 3.2
b = 4
error = 1

while error > 1e-5:
    c = (a + b)/2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    error = abs(b - a)

print("Raíz aproximada en [3.2,4]:", (a+b)/2)
