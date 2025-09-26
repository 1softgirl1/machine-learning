import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
["Гайка", "Gadget Hackwrench", "mouse", None],
["Дейл", "Dale", "chipmunk", "1"],
["Рокфор", "Monterey Jack", "mouse", "0.8"],
["Чип", "Chip", "chipmunk", "0.2"]]


print('1 задание')
df = pd.DataFrame(data, columns=['ru_name', 'en_name', 'class', 'cheer'])
df['cheer'] = df['cheer'].astype(float)
print(f"Тип данных cheer: {df['cheer'].dtype}")

print(df)

print('2 задание')
print(df.shape[0])

print('3 задание')
print(df.iloc[:, -1].count())

print('4 задание')
print(df.iloc[3, 1])

print('5 задание')
df1 = df.iloc[1:4, :3]
print(df1)

print('6 задание')
df.columns = ['ru_name', 'en_name', 'class', 'cheer']
print(df)

print('7 задание')
df['logcheer'] =  np.log(df['cheer'])
print(df)


print('8 задание')
x = df['class'].unique()
y = df['class'].value_counts().values
print(x, y)
plt.bar(x, y, color=['blue', 'green', 'red'])
plt.xlabel("class")
plt.ylabel("counts")
plt.title("frequency")
plt.show()
