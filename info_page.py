import pandas as pd
import numpy as np


def info(y):
    df = pd.read_csv(f'analysis/EtsySoldOrderItems{y}.csv')
    active_items = len(pd.unique(df['Item Name']))
    sold_count = df['Quantity'].sum()
    sold_sum = df['Item Total'].sum()
    df = df.groupby('Item Name')[['Quantity', 'Item Total']].sum()
    df = df.sort_values(by='Quantity', ascending=False)
    ten_count = list(df.iloc[:10]['Item Name'].values)
    df = df.sort_values(by='Item Total', ascending=False)
    ten_sold = list(df.iloc[:10]['Item Name'])
    return active_items, sold_count, sold_sum, ten_sold, ten_count