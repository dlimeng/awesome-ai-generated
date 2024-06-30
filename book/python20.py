import numpy as np
import matplotlib.pyplot as plt

# Define a heart-shaped function
def heart(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart(t)
plt.figure()
plt.plot(x, y, 'r-')
plt.xlim(-20, 20)
plt.title('Heart Curve')
plt.grid(True)
plt.show()