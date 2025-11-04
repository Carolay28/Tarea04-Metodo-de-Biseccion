import cmath

def f(x):
    if x == 3:
        return None  
    return ((x + 3)*(x + 1) * cmath.sqrt(x*(x - 1))) / (x - 3)

a = 0.01   
b = 2.4
error = 1

while error > 1e-5:
    c = (a + b)/2
    fa = f(a)
    fc = f(c)
    if fa.real * fc.real < 0:  
        b = c
    else:
        a = c
    error = abs(b - a)

print("Raíz aproximada en [-0.5,2.4]:", (a+b)/2)
