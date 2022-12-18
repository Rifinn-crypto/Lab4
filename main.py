import pandas as pd
import datetime
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import jerk


def main():
    df = pd.read_csv('dataset.csv')
    df.head()


    df.rename(columns={"Day": "day", "Exchange rate": "exchange_rate"}, inplace=True)
    df


    df.isnull().sum()


    df['deviation_from_median'] = abs(df['exchange_rate'] - df['exchange_rate'].median())
    df['deviation_from_avarege_value'] = abs(df['exchange_rate'] - df['exchange_rate'].mean())
    df


    jerk.filter_by_avg(pd, df['exchange_rate'].mean())
    

    jerk.sorted_by_dates(pd, '2022-9-15', '2020-02-02')

    jerk.sorted_by_month(pd, 2)
    def draw_weeks_stat(pd: pd.DataFrame, month: int) -> None:
     df['month'] = df['day'].dt.month
     sf = df[df['month'] == month]


     x = sf['exchange_rate']

     y1 = sf['exchange_rate'] - sf['exchange_rate'].mean()
     y2 = sf['exchange_rate'] - sf ['exchange_rate'].median()


     plt.ylabel('Exchange rate')
     plt.xlabel('Day')
     plt.plot(x, color='blue', linestyle='-.', linewidth=1, label='Exchange rate')
     plt.plot(y1, color='green', linestyle='-', linewidth=1, label='Deviation from avg')
     plt.plot(y2, color='red', linestyle='--', linewidth=1, label='Deviation from median')
     plt.legend()
     plt.title('Сurrency exchange rate changes over all time')
     plt.show()

jerk.draw_weeks_stat(df, 12)

if  == "__main__":
    main()








