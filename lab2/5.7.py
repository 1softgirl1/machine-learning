import matplotlib.pyplot as plt

vals = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
labels = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++ ']

explode = (0.1, 0, 0, 0, 0, 0)

plt.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1}, startangle=130)
plt.show()