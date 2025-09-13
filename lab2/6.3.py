import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y1 = 2*x
y2 = x*x

fig, axes = plt.subplots(1, 2, figsize=(10, 2))

axes[0].plot(x, y1, color='blue', linewidth=3)
axes[1].plot(x, y2, color='red', linestyle='--')
plt.show()