import pandas as pd
import numpy as np


def info(y, path):
    df = pd.read_csv(path + f'/EtsySoldOrderItems{y}.csv')
    active_items = len(pd.unique(df['Item Name']))
    sold_count = df['Quantity'].sum()
    sold_sum = df['Item Total'].sum()
    df = df.groupby('Item Name')[['Quantity', 'Item Total']].sum()
    df_1 = df.sort_values(by='Quantity', ascending=False)
    ten_count = pd.DataFrame(data=np.array([df_1.index]).T, columns=['Item Name']).iloc[:10]
    df_2 = df.sort_values(by='Item Total', ascending=False)
    ten_sold = pd.DataFrame(data=np.array([df_2.index]).T, columns=['Item Name']).iloc[:10]
    return active_items, sold_count, sold_sum, ten_sold, ten_count