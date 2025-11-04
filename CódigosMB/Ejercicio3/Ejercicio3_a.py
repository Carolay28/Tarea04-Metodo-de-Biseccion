import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 400)  
y1 = x
y2 = np.tan(x)

plt.figure(figsize=(8,5))
plt.plot(x, y1, label="y = x", color="blue")
plt.plot(x, y2, label="y = tan(x)", color="red")
plt.title("Gráficas de y = x y y = tan(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-10, 10)  
plt.grid(True)
plt.legend()
plt.show()
