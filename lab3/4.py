import numpy as np
import pandas as pd

print('1 задание')
polit = pd.read_csv('polit.csv', decimal=',')
polit = polit.dropna(how='all')
print(polit.head())

print('2 задание')
filtered_df = polit[polit['fh09'] > 5]
print(filtered_df)

print('3 задание')
print(polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)])

print('4 задание')
result = polit[((polit['afri'] == 1) + (polit['lati'] == 1)) > 1 & (polit['polity09'] > 8)]
print(result[['ctry', 'polity09', 'afri', 'lati']])

print('4 задание')
polit['corr_round'] = round(polit['corr0509'], 2)
print(polit[['ctry', 'corr_round', 'corr0509']])

print('5 задание')
polit['corr_round'] = round(polit['corr0509'], 2)
print(polit[['ctry', 'corr_round', 'corr0509']])

print('6 задание')
conditions = [
    (1.0 <= polit['fh09']) & (polit['fh09'] <= 2.5),
    (3.0 <= polit['fh09']) & (polit['fh09'] <= 5.0),
    (5.5 <= polit['fh09']) & (polit['fh09'] <= 7.0)
]

choices = ['Free', 'Partly Free', 'Not Free']
polit['fh_status'] = np.select(conditions, choices, default='Not categorized')
print(polit[['ctry', 'fh09', 'fh_status']])


print('7 задание')
grouped = polit.groupby('fh_status')
aggregated = grouped.agg({
    'gini': ['min', 'max', 'mean']
})
print(aggregated)


print('8 задание')
grouped8 = polit.groupby('fh_status')
for status, group_data in grouped8:
    filename = f"fh_status_{status.replace(' ', '_')}.csv"
    group_data.to_csv(filename, index=False, encoding='utf-8')


