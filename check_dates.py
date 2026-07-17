import sqlite3
import pandas as pd

db_path = 'C:/Users/User/Downloads/FloodSense_Mumbai/FloodSense_Mumbai/floodsense.db'
conn = sqlite3.connect(db_path)
df = pd.read_sql('SELECT Date, Confirmed_Event FROM rainfall_daily', conn)
conn.close()

df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

flood_dates = [
    "2018-06-08", "2018-06-25", "2018-07-10",
    "2019-07-02", "2019-07-26", "2019-09-04",
    "2020-08-04", "2020-08-05", "2020-08-06", "2020-09-22", "2020-09-24",
    "2021-05-17", "2021-06-09", "2021-06-13", "2021-07-16", "2021-07-18", "2021-07-22",
    "2022-07-05", "2022-08-16", "2022-10-07",
    "2023-06-24", "2023-07-20", "2023-07-26", "2023-07-27",
    "2024-07-08", "2024-07-26"
]

present_dates = []
missing_dates = []

for d in flood_dates:
    match = df[df['Date'] == d]
    if len(match) > 0:
        present_dates.append(d)
    else:
        missing_dates.append(d)

print("Present in rainfall_daily table (monsoon days):", len(present_dates))
print("Missing (not in 854 monsoon days):", len(missing_dates))
print("\nMissing dates list:", missing_dates)
