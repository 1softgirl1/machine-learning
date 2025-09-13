import matplotlib.pyplot as plt

vals = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
labels = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
plt.figure(figsize=(8, 6))

explode = (0.2, 0, 0, 0, 0, 0.1)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago",
          bbox={'facecolor': 'lightgray', 'edgecolor': 'black', })

plt.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1}, startangle=130)

plt.gca().set_aspect('auto')
plt.show()