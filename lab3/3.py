import pandas as pd
import matplotlib.pyplot as plt


print('1 задание')
df = pd.read_csv('la-crimes-sample.csv')
print(df)

print('2 задание')
print(df.shape[0])

print('3 задание')
print(df.dtypes)

print('4 задание')
print(df.nunique())

print('5 задание')
print(df.isnull().sum().sum())

print('6 задание')
print(df['Victim Sex'].value_counts())
f = (df['Victim Sex'] == 'F').sum()
m = (df['Victim Sex'] == 'M').sum()
if f > m:
    print('Жертв среди женщин больше, чем среди мужчин')
else:
    print('Жертв среди мужчин больше, чем среди женщин')

print('6 задание')
df6 = df['Crime Code Description'].value_counts().to_frame().iloc[:10]
print(df6)
df6.plot(grid=True, kind='bar', figsize=(10, 14))
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black', alpha=0.3)
plt.xticks(ha='right', fontsize=10)
plt.tight_layout()
plt.show()

print('6 задание')
sex_counts = df['Victim Sex'].value_counts()
for sex in ['F', 'M']:
    sex_data = df[df['Victim Sex'] == sex]
    top_crimes = sex_data['Crime Code Description'].value_counts().head(10)
    print(f"\nТОП-10 преступлений для {'женщин' if sex == 'F' else 'мужчин'}:")
    print(top_crimes)


print('6 задание')
print(df['Victim Descent'].value_counts()[:1])



print('7 задание')
area_crimes = df['Area Name'].value_counts().reset_index()
area_crimes.columns = ['Area Name', 'Crime Count']

area_crimes_sorted = area_crimes.sort_values('Crime Count', ascending=False)

print("Районы отсортированные по количеству преступлений (от самого опасного к самому безопасному):")
print(area_crimes_sorted)

colors = ['red' if x == area_crimes_sorted['Crime Count'].max() else
          'green' if x == area_crimes_sorted['Crime Count'].min() else
          'gray' for x in area_crimes_sorted['Crime Count']]

plt.barh(area_crimes_sorted['Area Name'], area_crimes_sorted['Crime Count'], color=colors)
plt.title('Самые опасные и безопасные районы', fontsize=14)
plt.xlabel('Количество преступлений')
plt.ylabel('Район')
plt.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()
