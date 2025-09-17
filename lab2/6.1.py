import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

centers = [1.5, 3.0, 4.5, 6.0, 7.5]
heights = [0.25, 0.02, 0.19, 0.25, 0.1]

data = []
for center, height in zip(centers, heights):
    n_points = int(height * 1000)
    data.extend(np.random.normal(center, 0.3, n_points))  

data = np.array(data)
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data, bins=5, density=True, color="pink", alpha=0.6, linewidth=1)


kde = gaussian_kde(data)
x_new = np.linspace(min(data), max(data), 200)
y_smooth = kde(x_new)

plt.plot(x_new, y_smooth, color="red", linewidth=2)

plt.ylim(0, 0.30)
plt.xlim(0, 10)
plt.yticks([0.00, 0.05, 0.10, 0.15, 0.20, 0.25])
plt.xticks([0, 2, 4, 6, 8])

plt.xlabel("petal_length")
plt.show()