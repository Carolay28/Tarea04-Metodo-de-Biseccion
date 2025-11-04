def f(x):
    return x**5 - x - 1

a = 1
b = 2
n_iter = 20

for _ in range(n_iter):
    c = (a + b)/2
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

raiz_aprox = (a + b)/2
print("Aproximación de la raíz:", round(raiz_aprox, 6))
