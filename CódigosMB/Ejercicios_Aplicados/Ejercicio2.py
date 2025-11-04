import math

s0 = 300      
m = 0.25      
k = 0.1       
g = 9.81      
tolerancia = 0.01

def s(t):
    return s0 - (m*g/k)*t + (m**2 * g / k**2)*(1 - math.exp(-k*t/m))

a = 0
b = 1000  
error = b - a

while error > tolerancia:
    c = (a + b)/2
    f_c = s(c)
    f_a = s(a)
    if f_a * f_c < 0:
        b = c
    else:
        a = c
    error = b - a

t_aprox = (a + b)/2
print("Tiempo aproximado de caída:", round(t_aprox, 2), "segundos")