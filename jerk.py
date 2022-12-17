import pandas as pd
import datetime

df = pd.read_csv('dataset.csv')
df.head()

df.rename(columns={"Day": "day", "Exchange rate": "exchange_rate"}, inplace=True)
df

df.isnull().sum()

df['deviation_from_median'] = abs(df['exchange_rate'] - df['exchange_rate'].median())
df['deviation_from_avarege_value'] = abs(df['exchange_rate'] - df['exchange_rate'].mean())
df

def filter_by_avg(pd: pd.DataFrame, value: int) -> pd.DataFrame:

pf = df[df['deviation_from_avarege_value'] >= value]
return pf

filter_by_avg(pd, df['exchange_rate'].mean())

def sorted_by_dates(pd: pd.DataFrame, data_from: str, data_to: str) -> pd.DataFrame:

df['day'] = pd.to_datetime(df['day'], format='%Y-%m')
pf = df.loc[(df['day'] <= data_from) & (df['day'] >= data_to)]
return pf

sorted_by_dates(pd, '2022-9-15', '2020-02-02')

from typing import Tuple

def sorted_by_month(pd: pd.DataFrame, month: int) -> Tuple[pd.DataFrame, int]:
df['month'] = df['day'].dt.month
pf = df[df['month'] == month]
return pf, pf['exchange_rate'].mean()

sorted_by_month(pd, 2)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df['day'] = pd.to_datetime(df['day'], format='%Y-%m-%d')
pf = df.loc[(df['day'] > '1998-01-01')]
pf
pf.plot(x = 'day', y = 'exchange_rate')
plt.ylabel('Exchange rate')
plt.xlabel('Day')
plt.title('Сurrency exchange rate changes over all time')
plt.show()

def draw_weeks_stat(pd: pd.DataFrame, month: int) -> None:
df['month'] = df['day'].dt.month
sf = df[df['month'] == month]


x = sf['exchange_rate']

y1 = sf['exchange_rate'] - sf['exchange_rate'].mean()
y2 = sf['exchange_rate'] - sf ['exchange_rate'].median()


x = sf['exchange_rate']

y1 = sf['exchange_rate'] - sf['exchange_rate'].mean()
y2 = sf['exchange_rate'] - sf ['exchange_rate'].median()

draw_weeks_stat(df, 12)