import pandas as pd
import numpy as np


def bascket_analysis():
    dfs = []
    for y in range(2015, 2020):
        exec(f'df = pd.read_csv("EtsySoldOrderItems{y}.csv")')
        dfs.append(df)

    Df_tr = dfs[0]
    for i in range(1, len(dfs)):
        Df_tr = Df_tr.append(dfs[i])