import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)

y1 = x**2 - 1
y2 = np.exp(1 - x**2)

plt.figure(figsize=(8,5))
plt.plot(x, y1, label="y = x^2 - 1", color="blue")
plt.plot(x, y2, label="y = e^(1 - x^2)", color="red")
plt.title("Gráficas de y = x^2 - 1 y y = e^(1 - x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
