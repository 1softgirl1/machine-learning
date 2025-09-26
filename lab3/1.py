import pandas as pd

series_obj = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

print('1 задание')
print(series_obj)

print('2 задание')
print(series_obj.loc['d'])

print('3 задание')
print(series_obj.iloc[1])

print('4 задание')
series_obj['f'] = 6
print(series_obj)

print('5 задание')
print(series_obj[2:5].values)

print('6 задание')
data = [[1, 2], [5, 3], [3.7, 4.8]]
df = pd.DataFrame(data, columns=['col1', 'col2'])
print(df)

print('6 задание')
print(df['col1'][2])

print('7 задание')
df.iloc[1, 1] = 9
print(df)

print('8 задание')
print(df.iloc[1:])

print('9 задание')
df['col3'] = df['col1'] * df['col2']
print(df)

