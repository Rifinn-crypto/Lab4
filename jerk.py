import pandas as pd
import datetime
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def filter_by_avg(pd: pd.DataFrame, value: int) -> pd.DataFrame:
        
        pf = df[df['deviation_from_avarege_value'] >= value]
        return pf

def sorted_by_dates(pd: pd.DataFrame, data_from: str, data_to: str) -> pd.DataFrame:
    df['day'] = pd.to_datetime(df['day'], format='%Y-%m')
    pf = df.loc[(df['day'] <= data_from) & (df['day'] >= data_to)]
    return pf

def sorted_by_month(pd: pd.DataFrame, month: int) -> Tuple[pd.DataFrame, int]:
    df['month'] = df['day'].dt.month
    pf = df[df['month'] == month]
    return pf, pf['exchange_rate'].mean()

def draw_weeks_stat(pd: pd.DataFrame, month: int) -> None:
    df['month'] = df['day'].dt.month
    sf = df[df['month'] == month]

    x = sf['exchange_rate']

    y1 = sf['exchange_rate'] - sf['exchange_rate'].mean()
    y2 = sf['exchange_rate'] - sf ['exchange_rate'].median()

