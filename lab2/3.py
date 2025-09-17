import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 4, 400)
y = x**2 - x - 6

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y(x) = x² - x - 6')

plt.axhline(y=0, color='r', linestyle='--', alpha=0.7, label='y = 0')


plt.scatter([-2, 3], [0, 0], color='red', s=100, zorder=5, label='Точки пересечения')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('График функции y(x) = x² - x - 6')
plt.grid(True, alpha=0.3)
plt.legend()

plt.xlim(-3, 4)
plt.ylim(-8, 6)

plt.tight_layout()
plt.show()
