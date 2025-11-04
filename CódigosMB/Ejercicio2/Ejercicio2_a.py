import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400) 

y1 = x
y2 = np.sin(x)

plt.figure(figsize=(8,5))
plt.plot(x, y1, label="y = x", color="blue")
plt.plot(x, y2, label="y = sin(x)", color="red")
plt.title("Gráficas de y = x y y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()