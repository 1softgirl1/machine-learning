import numpy as np
import pandas as pd

print('1 задание')
df = pd.read_csv(
    "data.txt",
    sep=";",
    header=None,
    na_values=' ',
    names=['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall']
)

print(df.head())
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

print('2 задание')
df.drop('index', axis=1, inplace=True)
print(df.head())

print('3 задание')
print(df.info())
# Если в столбце "Non-Null Count" количество значений меньше общего количества строк,
# то есть пропущенные значения


print('4 задание')

if 'year' in df.columns:
    missing_by_year = df.groupby('year').size() - df.groupby('year').count()
    print(missing_by_year)
    total_missing_by_year = missing_by_year.sum(axis=1)

    print(total_missing_by_year)

    year_with_most_missing = total_missing_by_year.idxmax()
    print(f"\nБольше всего пропусков в данных за {year_with_most_missing} год")



print('5 задание')
df["date"] = pd.to_datetime(df[["year", "month", "day"]])
print(df)
print(df.dtypes)

print('6 задание')
for col in ['min_t', 'average_t', 'max_t', 'rainfall']:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["temp_range"] = df["max_t"] - df["min_t"]

dry_days_count = []
count = 0
for rain in df["rainfall"]:
    if pd.isna(rain) or rain == 0:
        dry_days_count.append(count)
        count += 1
    else:
        dry_days_count.append(count)
        count = 0

df["prev_dry_days"] = dry_days_count
print(df)

print('7 задание')
print(df["prev_dry_days"].max())

print('8 задание')
yearly_stats = df.groupby('year').agg({
    'average_t': 'mean',
    'rainfall': 'sum'
})

avg_temp_by_year = yearly_stats['average_t']
total_rainfall_by_year = yearly_stats['rainfall']

print(avg_temp_by_year)
print(total_rainfall_by_year)

warmest_year = avg_temp_by_year.idxmax()
coldest_year = avg_temp_by_year.idxmin()
print(f"Самый теплый год: {warmest_year} (средняя температура: {avg_temp_by_year.max():.2f}°C)")
print(f"Самый холодный год: {coldest_year} (средняя температура: {avg_temp_by_year.min():.2f}°C)")

wettest_year = total_rainfall_by_year.idxmax()
driest_year = total_rainfall_by_year.idxmin()
print(f"Год с наибольшим количеством осадков: {wettest_year} (осадки: {total_rainfall_by_year.max():.2f} мм)")
print(f"Год с наименьшим количеством осадков: {driest_year} (осадки: {total_rainfall_by_year.min():.2f} мм)")


print('9 задание')
condition1 = df['average_t'] < -30
cold_days = df[condition1]
print(f"Дней со средней температурой ниже -30°C: {len(cold_days)}")
if len(cold_days) > 0:
    print(cold_days[['date', 'average_t']])


condition2 = (df['average_t'] > 27) & (df['prev_dry_days'] > 3)
hot_dry_days = df[condition2]
print(f"\nДней с температурой выше 27°C и засухой более 3 дней: {len(hot_dry_days)}")
if len(hot_dry_days) > 0:
    print(hot_dry_days[['date', 'average_t', 'prev_dry_days']])