import matplotlib.pyplot as plt
import numpy as np

# 1
x = [0, 10, 50]
y = [0, 30, 150]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line')
plt.show()

# 2
x1 = [0, 20, 30]
y1 = [20, 40, 0]
plt.plot(x1, y1, color='blue', linewidth=3, label='line1-width-3)')
x2 = [0, 20, 30]
y2 = [40, 0, 30]
plt.plot(x2, y2, color='red', linewidth=5, label='line2-width-5')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines with different widths and colors with suitable legends')
plt.legend(loc='upper right')
plt.show()

# 3
x2 = [0, 20, 30]
y2 = [20, 40, 0]
plt.plot(x2, y2, linestyle='dotted', color='blue', linewidth=3, label='line1-dotted')
x1 = [0, 20, 30]
y1 = [40, 0, 30]
plt.plot(x1, y1, linestyle='dashed', color='red', linewidth=5, label='line2-dashed')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Plot with two or more lines with different styles')
plt.legend(loc='upper right')
plt.show()

# 4
x1 = [1, 4, 5, 6, 7]
y1 = [2, 6, 3, 6, 3]
plt.plot(x1, y1, linestyle='dashdot', color='red',  marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display marker')
plt.show()

# 5
x1 = [2, 3, 5, 6, 8]
y1 = [2, 5, 10, 22, 20]
plt.plot(x1, y1, linestyle=' ', marker='o', markersize=5, markerfacecolor='red', markeredgecolor='red')
x2 = [3, 4, 6, 7, 9]
y2 = [3, 6, 11, 19, 21]
plt.plot(x2, y2, linestyle=' ', marker='*', markersize=5, markerfacecolor='blue', markeredgecolor='blue')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display marker')
plt.show()

# 6
dates = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
values = [772.56, 776.43, 776.47, 777.07, 775.08]
plt.plot(dates, values, color='red', marker='o')

plt.title('Closing stock value of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Value')

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.5)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)
plt.ylim(772.5, 777.2)
plt.yticks(np.arange(772.5, 777.2, 0.5))

plt.show()