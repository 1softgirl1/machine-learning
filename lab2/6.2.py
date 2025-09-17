import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

x = range(100)
y = [i*2 for i in x]

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")

ax_inset = inset_axes(ax, width="30%", height="30%", loc='center right')

ax_inset.plot(x, y)
ax_inset.set_xlabel("x")
ax_inset.set_ylabel("y")

ax_inset.set_xticks([0, 100])
ax_inset.set_yticks([0, 200])

plt.show()
