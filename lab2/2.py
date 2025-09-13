import matplotlib.pyplot as plt
import numpy as np

x1 = [2, 3, 5, 6, 8]
y1 = [2, 5, 10, 22, 20]

plt.plot(x1, y1, linestyle=' ', marker='o', markersize=5, markerfacecolor='red', markeredgecolor='red')

plt.ylim(0, 4)
plt.yticks(np.arange(0, 4, 0.25))


plt.xlim(0, 4)
plt.xticks(np.arange(0, 4, 0.25))

plt.xlabel('Подпись оси OX')
plt.ylabel('Подпись оси OY')
plt.title('Элементы изображения')

plt.grid(True, which='major', linestyle='-', alpha=0.3)
plt.grid(True, which='minor', linestyle=':', alpha=0.2)


plt.show()
