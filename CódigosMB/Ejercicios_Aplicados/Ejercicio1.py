import math

L = 10
r = 1
V_deseado = 12.4
tolerancia = 0.01

def V(h):
    return L * (0.5*math.pi*r**2 - r**2*math.asin(h/r) - h*math.sqrt(r**2 - h**2))

a = 0
b = r
error = b - a

while error > tolerancia:
    c = (a + b)/2
    f_c = V(c) - V_deseado
    f_a = V(a) - V_deseado
    if f_a * f_c < 0:
        b = c
    else:
        a = c
    error = b - a

h_aprox = (a + b)/2
print("Profundidad aproximada del agua es h =", round(h_aprox, 2), "cm")
