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


    filter_by_avg(pd, df['exchange_rate'].mean())
    

    sorted_by_dates(pd, '2022-9-15', '2020-02-02')

    sorted_by_month(pd, 2)
    df['day'] = pd.to_datetime(df['day'], format='%Y-%m-%d')
    pf = df.loc[(df['day'] > '1998-01-01')]
    pf
    pf.plot(x = 'day', y = 'exchange_rate')
    plt.ylabel('Exchange rate')
    plt.xlabel('Day')
    plt.title('Сurrency exchange rate changes over all time')
    plt.show()
    draw_weeks_stat(df, 12)
if  == "__main__":
    main()








